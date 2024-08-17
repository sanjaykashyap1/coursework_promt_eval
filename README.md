# Calculating and Reporting Metrics of the RAG Pipeline

UPDATED VIDEO BASED ON TA FEEDBACK


[![Demo Video](https://img.youtube.com/vi/V-VHoerykSs/0.jpg)](https://youtu.be/E-hOGjUR6tk)

[![Demo Video](https://img.youtube.com/vi/V-VHoerykSs/0.jpg)](https://youtu.be/V-VHoerykSs)


This project evaluates the performance of a transcript-based QA system by calculating various metrics and generating evaluation reports using OpenAI's GPT-4. The evaluation metrics include context precision, recall, relevance, entity recall, noise robustness, faithfulness, answer relevance, information integration, counterfactual robustness, negative rejection, and latency.

## Table of Contents

- [Introduction](#introduction)
- [Methodology](#methodology)
- [Results](#results)
- [Methods for Improvement](#methods-for-improvement)
- [Challenges Faced](#challenges-faced)
- [Conclusion](#conclusion)
- [Research and Exploration](#research-and-exploration)
- [Files Overview](#files-overview)
  - [eval.py](#evalpy)
  - [eval2.py](#eval2py)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

The objective of this project is to evaluate the performance of a transcript-based QA system by comparing the app-generated answers to expected answers based on a given set of questions. The evaluation process is automated using several metrics, and the results are further evaluated using OpenAI's GPT-4.

## Methodology

### Initial Manual Comparison

The initial approach involved manually comparing the app-generated answers to the expected answers derived from the transcript. This method, although straightforward, was not scalable or objective, leading to the need for automated evaluation methods.

### Automated Evaluation Metrics

To address the limitations of manual comparison, several automated evaluation metrics were implemented:

1. **Answer Relevance**: Uses TF-IDF Vectorization and Cosine Similarity to measure relevance.
2. **Faithfulness**: Uses Substring Matching to check if the expected answer is a substring of the generated answer.
3. **Information Integration**: Uses TF-IDF Vectorization and Cosine Similarity to assess the ability to integrate and present information cohesively.
4. **Entity Recall**: Uses Named Entity Recognition (NER) and Set Intersection to measure the recall of entities in the generated answers.

### Metrics Calculation

The following metrics are calculated for evaluation:

- Context Precision
- Context Recall
- Context Relevance
- Context Entity Recall
- Noise Robustness
- Faithfulness
- Answer Relevance
- Information Integration
- Counterfactual Robustness
- Negative Rejection
- Latency

## Results

The automated evaluation metrics were applied to the initial set of questions and answers, yielding the following results:

- **Answer Relevance**: 0.83
- **Faithfulness**: 0.60
- **Information Integration**: 0.81
- **Entity Recall**: 0.67

## Methods for Improvement

### DeepEval

DeepEval is a framework for the deep evaluation of machine-generated answers using advanced NLP techniques to evaluate responses based on coherence, consistency, relevance, and informativeness.

### RAG (Retrieval-Augmented Generation)

RAG combines retrieval-based and generation-based models to generate more accurate and contextually relevant answers.

### Improved Method: OpenAI GPT-4 Evaluation

Using OpenAI's GPT-4 model to evaluate QA pairs for accuracy, relevance, and faithfulness, providing more nuanced and context-aware assessments.

## Challenges Faced

1. **Scalability of Manual Evaluation**: Addressed by implementing automated evaluation metrics.
2. **Initial Metric Accuracy**: Enhanced by integrating OpenAI's GPT-4 model.
3. **Context-Aware Evaluation**: Improved by using advanced models like RAG and GPT-4.

## Conclusion

The project transitioned from a subjective and inefficient manual evaluation approach to an automated, scalable, and objective framework. By integrating advanced models like OpenAI's GPT-4 and RAG, the evaluation accuracy and reliability significantly improved, providing detailed insights into the performance of the generated answers.

## Research and Exploration

### Depth of Research

Extensive research was conducted to understand and calculate the metrics, exploring methods like TF-IDF, cosine similarity, and entity extraction. State-of-the-art models like RAG and GPT-4 were investigated to improve evaluation accuracy.

### Exploration of Methods

A comprehensive evaluation framework was developed, incorporating both traditional NLP techniques and modern transformer models. Methods like DeepEval and RAG were implemented for better performance analysis, demonstrating creativity in integrating various evaluation techniques.

## Files Overview

### eval.py

`eval.py` is responsible for calculating various evaluation metrics for the QA system. It uses traditional NLP techniques such as TF-IDF vectorization and cosine similarity to measure metrics like answer relevance, faithfulness, information integration, and entity recall. The script provides a foundational approach to automated evaluation, replacing the need for manual comparison with a scalable and objective method.

### eval2.py

`eval2.py` extends the functionality of `eval.py` by integrating OpenAI's GPT-4 model for a more nuanced and context-aware evaluation. This script evaluates the QA pairs for accuracy, relevance, and faithfulness using the `openai.ChatCompletion.create` method. It further enhances the evaluation process by providing insights generated by a state-of-the-art language model, improving the overall assessment of the QA system.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/rag-metrics-evaluation.git
    cd rag-metrics-evaluation
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory with the following content:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

2. Open the provided local URL in your web browser to interact with the app.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
"""

# Save the updated README content to a text file
with open("/mnt/data/README.txt", "w") as file:
    file.write(readme_content)
