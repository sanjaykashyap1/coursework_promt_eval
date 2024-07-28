import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Define questions, expected answers, and app-generated answers
qa_pairs = [
    ("What's the issue reported by Al Grover?", "There's a leak coming through his kitchen ceiling.", "There is a leak coming through his kitchen ceiling."),
    ("What is Charlie Johnson's problem?", "He received the wrong color scarf", "Charlie Johnson's problem is that he received the wrong color Parker scarf for his wife's birthday and needs to exchange it for the correct color"),
    ("Why is Ron calling Regency limousine?", "His limo is 30 minutes late", "Ron is calling Regency limousine because his daughter's limo for her senior prom is 30 minutes late and he wants to speak to someone about it."),
    ("What did Steve Simmons want to do with the blender?", "He wants to return a recalled blender and get a different model.", "He wanted to return it and get a different model due to a recall on the current model."),
    ("Why is Jeff Matthews complaining?", "His neighbors are being loud and disturbing his newborn baby.", "Jeff Matthews is complaining because his neighbors are being loud and disturbing his newborn baby's sleep."),
    ("What is the callback number for Al Grover?", "610-265-1714", "610-265-1714"),
    ("What is Al Grover's apartment number?", "E 107", "E 107"),
    ("What is Steve Simmons' email address?", "stevesimmons@gmail.com", "stevesimmons@gmail.com"),
    ("What is the zip code of King of Prussia mentioned in the transcript?", "19406", "19406"),
    ("Who was supposed to arrive at Al Grover's apartment?", "The maintenance man.", "The maintenance man, Drake"),
    ("What model number of the blender was recalled?", "23087", "23087"),
    ("What color Parker scarf did Charlie Johnson receive?", "Light blue.", "Light blue."),
    ("What color Parker scarf did Charlie Johnson want?", "Royal blue", "The darker one, specifically the royal blue color."),
    ("What is Jeff Matthews' complaint about his neighbors?", "They are being loud and disturbing his newborn baby's sleep.", "They are being loud and disturbing his newborn baby's sleep."),
    ("How soon did the customer service representative say the new blender would arrive?", "In about four to six business days.", "The customer service representative said the new blender would arrive in about four to six business days.")
]

questions, expected_answers, generated_answers = zip(*qa_pairs)

def calculate_answer_relevance(questions, generated_answers):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(questions + generated_answers)
    relevances = [
        cosine_similarity(tfidf_matrix[i:i+1], tfidf_matrix[len(questions)+i:len(questions)+i+1])[0][0]
        for i in range(len(questions))
    ]
    return np.mean(relevances)

def calculate_faithfulness(expected_answers, generated_answers):
    return sum(1 for e, g in zip(expected_answers, generated_answers) if e.lower() in g.lower()) / len(expected_answers)

def calculate_information_integration(expected_answers, generated_answers):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(expected_answers + generated_answers)
    integration_scores = [
        cosine_similarity(tfidf_matrix[i:i+1], tfidf_matrix[len(expected_answers)+i:len(expected_answers)+i+1])[0][0]
        for i in range(len(expected_answers))
    ]
    return np.mean(integration_scores)

def calculate_entity_recall(expected_answers, generated_answers):
    def extract_entities(text):
        return set(re.findall(r'\b[A-Z][a-z]*\b', text))

    expected_entities = [extract_entities(a) for a in expected_answers]
    generated_entities = [extract_entities(a) for a in generated_answers]
    recalls = [
        len(gen.intersection(exp)) / len(exp) if exp else 1
        for gen, exp in zip(generated_entities, expected_entities)
    ]
    return np.mean(recalls)

# Calculate metrics
answer_relevance = calculate_answer_relevance(questions, generated_answers)
faithfulness = calculate_faithfulness(expected_answers, generated_answers)
information_integration = calculate_information_integration(expected_answers, generated_answers)
entity_recall = calculate_entity_recall(expected_answers, generated_answers)

# Print results
print(f"Answer Relevance: {answer_relevance:.2f}")
print(f"Faithfulness: {faithfulness:.2f}")
print(f"Information Integration: {information_integration:.2f}")
print(f"Entity Recall: {entity_recall:.2f}")

# Print comparison of expected and generated answers
print("\nComparison of Expected and Generated Answers:")
for q, e, g in zip(questions, expected_answers, generated_answers):
    print(f"Q: {q}")
    print(f"Expected: {e}")
    print(f"Generated: {g}")
    print()