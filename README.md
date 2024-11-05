# NLP_Assignment_2
Assignment 2: Regular Expressions Report
Introduction
In this assignment, we focus on building an algorithm to resolve context-related ambiguities in language, perform sentiment analysis, and evaluate the performance of the sentiment analysis using metrics like accuracy, precision, and recall. The key components include a sentiment analysis class and a performance evaluation class.
Functionality Overview
1. Context Disambiguation
•	What it Does: The algorithm identifies different meanings of the word "Apple" based on the context (e.g., as a fruit vs. as a company).
•	Input: A sentence containing the ambiguous term (e.g., "I love eating an apple" vs. "Apple released a new product").
•	Output: A resolved meaning based on context (e.g., "fruit" or "company").
2. Sentiment Analysis
•	What it Does: The SentimentAnalyzer class analyzes text to determine its sentiment based on the frequency of positive and negative words.
•	Input: A list of sentences (e.g., ["I love this product!", "This is bad."]).
•	Output: The overall sentiment classification (e.g., "Positive", "Negative", or "Neutral").
3. Performance Evaluation
•	What it Does: The PerformanceEvaluator class calculates the accuracy, precision, and recall of the sentiment analysis results.
•	Input: True positives (TP), false positives (FP), and false negatives (FN) as integers (e.g., tp = 30, fp = 5, fn = 10).
•	Output: A tuple containing performance metrics (e.g., (accuracy, precision, recall)).
