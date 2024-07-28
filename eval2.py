import streamlit as st
import pandas as pd
import openai
import numpy as np
import streamlit as st
import pandas as pd
import openai
import numpy as np
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up your OpenAI API key
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
# Hardcoded data
data = {
    "Question": [
        "What's the issue reported by Al Grover?",
        "What is Charlie Johnson's problem?",
        "Why is Ron calling Regency limousine?",
        "What did Steve Simmons want to do with the blender?",
        "Why is Jeff Matthews complaining?",
        "What is the callback number for Al Grover?",
        "What is Al Grover's apartment number?",
        "What is Steve Simmons' email address?",
        "What is the zip code of King of Prussia mentioned in the transcript?",
        "Who was supposed to arrive at Al Grover's apartment?",
        "What model number of the blender was recalled?",
        "What color Parker scarf did Charlie Johnson receive?",
        "What color Parker scarf did Charlie Johnson want?",
        "What is Jeff Matthews' complaint about his neighbors?",
        "How soon did the customer service representative say the new blender would arrive?"
    ],
    "Expected answer": [
        "There's a leak coming through his kitchen ceiling.",
        "He received the wrong color scarf",
        "His limo is 30 minutes late",
        "He wants to return a recalled blender and get a different model.",
        "His neighbors are being loud and disturbing his newborn baby.",
        "610-265-1714",
        "E 107",
        "stevesimmons@gmail.com",
        "19406",
        "The maintenance man.",
        "23087",
        "Light blue.",
        "Royal blue",
        "They are being loud and disturbing his newborn baby's sleep.",
        "In about four to six business days."
    ],
    "App generated answer": [
        "There is a leak coming through his kitchen ceiling.",
        "Charlie Johnson's problem is that he received the wrong color Parker scarf for his wife's birthday and needs to exchange it for the correct color",
        "Ron is calling Regency limousine because his daughter's limo for her senior prom is 30 minutes late and he wants to speak to someone about it.",
        "He wanted to return it and get a different model due to a recall on the current model.",
        "Jeff Matthews is complaining because his neighbors are being loud and disturbing his newborn baby's sleep.",
        "610-265-1714",
        "E 107",
        "stevesimmons@gmail.com",
        "19406",
        "The maintenance man, Drake",
        "23087",
        "Light blue.",
        "The darker one, specifically the royal blue color.",
        "They are being loud and disturbing his newborn baby's sleep.",
        "The customer service representative said the new blender would arrive in about four to six business days."
    ]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Hardcoded transcript
transcript = """
This call is now being recorded. Good evening, Valley View apartments. Hi. There's a leak coming through my kitchen ceiling. Oh, okay. Let me page our maintenance man. May I have your first name, please? Sure. It's Al. And your last name? Grover. G r o v e R. Okay. And your apartment number? E 107. That's e 107? Yes. Okay. And a callback number? 610-265-1714 and you said there's a leak coming through your kitchen ceiling? Yeah, it's a little bit more than a drip, so if you could get somebody out here as soon as possible. No problem. I will page him right away, and you'll be hearing from him shortly. Thank you very much. You're welcome. Bye bye. This call is now being recorded. Parker scarves, how may I help you? I bought a scarf online for my wife, and it turns out they shipped the wrong color. Oh, I am so sorry, sir. I got it for a birthday, which is tonight, and now I'm not 100% sure what I need to do. Okay, let me see if I can help you. Do you have the item number of the Parker scarf? I don't think so. It's called a New Yorker, I think. Excellent. Okay. What color did you want the New Yorker in? Blue. The one they shipped was light blue. I wanted the darker one. Did you want navy blue or royal blue? What's the difference? There? The royal blue is a bit brighter. That's the one I want. Okay. What zip code are you located in? 19406. It appears that we do not. I'm sorry. That we do have that item in stock at Karen's boutique at the Hunter mall. Is that close by? It is. It's right by my office. Okay. What is your name, sir? Charlie Johnson. Charlie Johnson. Is that j o h n? S o n? Yes, ma'am. And Mister Johnson, do you have the Parker scarf in light blue with you now? I do. They shipped it to my office. It just came in not that long ago. Okay. What I will do is make arrangements with Karen's boutique for you to exchange the Parker scarf at no additional cost. And in addition, I was able to look up your order in our system, and I'm going to send out a special gift to you to make up for the inconvenience. Oh, excellent. Thank you so much. You're welcome. And thank you for calling Parker Scarf, and I hope your wife enjoys her birthday gift. Thank you. Thank you very much. You're very welcome. Goodbye. This call is now being recorded. Regency limousine. This is Gina. May I help you? Yeah, hi. I'm waiting for my limo to show up. It's about 30 minutes late already. Oh, I'm so sorry about that. If you could give me the pickup time and location, we can get this settled for you. My daughter's going to her senior prom. They're already a half an hour late. I need to speak to someone. I totally understand, and we're truly sorry. I'll have someone there as soon as possible. What time was the pickup? 06:00 okay, and the location? 800 North Henderson Road. 800 North Henderson road. Yes. And the town and zip code, please? King of Prussia, 19406. That's king of Prussia 19406. Yes. Okay, and am I speaking with Ron? Yes. Okay, if you don't mind staying on the line for just a moment. Drake is scheduled as your driver. I'm going to give him a call and I'll find out his whereabouts. Okay, this better not take long. Just a minute, please. Hello? Mister Mendez? Yes, I spoke with Drake. He will be there in five minutes. He's supposed to be here half an hour ago. If he doesn't show up in five minutes, he was stuck in traffic, but he is now on first Avenue in king of Prussia and will be there momentarily. All right, I. Oh, and I'm so sorry about the delay. Thanks for your help. You're welcome. Goodbye. Call is now being recorded. Johnson appliances, this is Alex. How can I help you? Hi, I recently purchased a blender from you guys, and I just got an email saying that there's a recall on the model because one of the blades are defective, so I want to return it and get a different model. Sure, sir, I can definitely help you with that. What is your first and last name? Steve Simmons. Okay, can you spell that for me? S t e v e. Last name is Simmons. S I m m o n s. Okay, I have Steve. S t e v e. Simmons. S I m m o m s. Correct. Okay, can I also have your email address? Sure. It's stevesimmons, just like it's spelled@gmail.com. okay, I have stevesimmons. Stevesimmons. Mail.com. yes. Okay, great. I have located you in our system, and you purchased the model number 230 eight seven, which has been recalled. I'm going to email you a prepaid shipping label to send back the recalled blender, and we will be mailing you our latest model. Oh, thank you very much. No problem. Mister Simmons. Can I just have your mailing address? Sure. It's 800 North Henderson Road in king of Prussia, Pennsylvania. And the zip is 1946. Okay, I have 800 North Henderson Road king of Prussia, Pennsylvania, 19406. Correct. And could you tell me how long it's going to take to get the new blender? Sure. You can expect your new blender to arrive in about four to six business days. Oh, great. Thank you very much. No problem. Is there anything else I can help you with today? No, that's all I needed. But thank you. Thank you. Have a nice day. You too. Bye bye. Bye bye. Call is now being recorded. Good evening, Kingfoot apartments. This is Alex. How may I help you? Hey, yeah, I'm in apartment 104 on the first floor. I'm calling to complain about my neighbors. Okay, what seems to be the problem, sir? It's very late. I just got my newborn baby to sleep, and they're being loud again. I brought this to their attention several times, but they never, you know, never stops. Okay, I'm very sorry about that. Just let me take down your contact information. I'll contact the landlord right away to get this all straightened out. Okay. My name is Jeff Matthews. Okay, Mister Matthews. Can you spell that for me? First name is Jeff. J E f f. Last name is Matthews. M a p t h e w s. Okay, Mister Matthews, can I have the best number you can be reached at and also your apartment number again? Sure. It's 610,260. 517 14. And I'm in department 104 on the first floor. Okay, I have 610-265-1714 and apartment 104. Yes. All right, Mister Matthews, I'm going to pass this information on to the landlord right away and he'll be contacting you shortly. Is there anything else I can help you with today? No, that's all. Thank you. Thank you very much. Have a great night. You too.
"""

def evaluate_answers(generated_answers, expected_answers):
    exact_matches = 0
    partial_matches = 0

    for generated, expected in zip(generated_answers, expected_answers):
        if generated.lower() == expected.lower():
            exact_matches += 1
        elif expected.lower() in generated.lower():
            partial_matches += 1

    return exact_matches, partial_matches

def calculate_metrics(df):
    total_questions = len(df)
    exact_matches, partial_matches = evaluate_answers(df['App generated answer'], df['Expected answer'])

    context_precision = exact_matches / total_questions
    context_recall = (exact_matches + partial_matches) / total_questions
    context_relevance = (exact_matches + partial_matches / 2) / total_questions
    context_entity_recall = context_recall
    noise_robustness = context_precision  # Simplified for this example

    faithfulness = context_precision
    answer_relevance = context_relevance
    information_integration = context_relevance
    counterfactual_robustness = 1 - context_precision  # Simplified for this example
    negative_rejection = 1 - context_precision  # Simplified for this example
    latency = np.random.uniform(0.5, 2.0)  # Random value for this example

    metrics = {
        "Context Precision": context_precision,
        "Context Recall": context_recall,
        "Context Relevance": context_relevance,
        "Context Entity Recall": context_entity_recall,
        "Noise Robustness": noise_robustness,
        "Faithfulness": faithfulness,
        "Answer Relevance": answer_relevance,
        "Information Integration": information_integration,
        "Counterfactual Robustness": counterfactual_robustness,
        "Negative Rejection": negative_rejection,
        "Latency": latency
    }

    return metrics

def openai_evaluate(df):
    evaluation_results = []
    for _, row in df.iterrows():
        question = row["Question"]
        expected_answer = row["Expected answer"]
        generated_answer = row["App generated answer"]

        prompt = f"""
        Evaluate the following QA pair:

        Question: {question}

        Expected Answer: {expected_answer}

        Generated Answer: {generated_answer}

        Please provide an evaluation considering accuracy, relevance, and faithfulness.
        """
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that evaluates QA pairs."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        evaluation_results.append(response.choices[0].message.content.strip())

    return evaluation_results

# Streamlit app
st.title("Transcript Evaluation App")

if st.button("Generate and Evaluate Answers"):
    st.write("Generated Answers and Evaluation:")
    st.write(df)

    metrics = calculate_metrics(df)
    st.write("Performance Metrics:")
    st.write(metrics)

    openai_evaluations = openai_evaluate(df)
    df["OpenAI Evaluation"] = openai_evaluations
    st.write("OpenAI Evaluation Results:")
    st.write(df)
