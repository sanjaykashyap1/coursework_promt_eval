import pandas as pd
import numpy as np
from sklearn.metrics import precision_score, recall_score

# Define a function to calculate evaluation metrics
def calculate_metrics(expected, generated):
    # Initialize metrics
    precision = recall = relevance = entity_recall = faithfulness = answer_relevance = 0.0
    
    # Calculate precision and recall
    precision = precision_score([expected], [generated], average='micro')
    recall = recall_score([expected], [generated], average='micro')
    
    # Simulate other metrics (in a real scenario, you would have different logic for these)
    if expected.lower() in generated.lower():
        relevance = entity_recall = faithfulness = answer_relevance = 1.0
    
    return precision, recall, relevance, entity_recall, faithfulness, answer_relevance

# Define latency function (simulated here as a constant low value for demonstration)
def get_latency():
    return np.random.uniform(0.1, 0.3)  # Simulated latency in seconds

# Data preparation (provided manually for demonstration)
data = {
    'Question': [
        "What's the issue reported by Al Grover?",
        "What is Charlie Johnson's problem?",
        "Why is Ron calling Regency limousine?",
        "What did Steve Simmons want to do with the blender?",
        "Why is Jeff Matthews complaining?"
    ],
    'Expected Answer': [
        "There's a leak coming through his kitchen ceiling.",
        "He received the wrong color scarf",
        "His limo is 30 minutes late",
        "He wants to return a recalled blender and get a different model.",
        "His neighbors are being loud and disturbing his newborn baby."
    ],
    'App Generated Answer': [
        "There is a leak coming through his kitchen ceiling.",
        "Charlie Johnson's problem is that he received the wrong color Parker scarf for his wife's birthday and needs to exchange it for the correct color",
        "Ron is calling Regency limousine because his daughter's limo for her senior prom is 30 minutes late and he wants to speak to someone about it.",
        "He wanted to return it and get a different model due to a recall on the current model.",
        "Jeff Matthews is complaining because his neighbors are being loud and disturbing his newborn baby's sleep."
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize columns for metrics
metrics_columns = ['Precision', 'Recall', 'Relevance', 'Entity Recall', 'Faithfulness', 'Answer Relevance', 'Latency']
for col in metrics_columns:
    df[col] = 0.0

# Evaluate each answer
for index, row in df.iterrows():
    expected = row['Expected Answer']
    generated = row['App Generated Answer']
    precision, recall, relevance, entity_recall, faithfulness, answer_relevance = calculate_metrics(expected, generated)
    latency = get_latency()
    
    df.at[index, 'Precision'] = precision
    df.at[index, 'Recall'] = recall
    df.at[index, 'Relevance'] = relevance
    df.at[index, 'Entity Recall'] = entity_recall
    df.at[index, 'Faithfulness'] = faithfulness
    df.at[index, 'Answer Relevance'] = answer_relevance
    df.at[index, 'Latency'] = latency

# Display the evaluated DataFrame
print(df)

# Optionally, save the evaluated results to a CSV file
df.to_csv('evaluated_results.csv', index=False)
