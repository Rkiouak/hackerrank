Link: https://www.hackerrank.com/challenges/document-classification

Note: I think the hackerrank indicator for success on this one is too highly tuned:
this returns a hr calculated accuracy score (percent labels correct on test set)
of 93.42, but they don't mark as completed until 94.70. I would need to look more closely
at the test set to see if theres any obvious potential PCA or Ada boosting/ther multi classifier chaining
I could do to improve score.

You have been given a stack of documents that have already been processed and some that have not. Your task is to classify these documents into one of eight categories: [1,2,3,...8]. You look at the specifications on what a document must contain and are baffled by the jargon. However, you notice that you already have a large amount of documents which have already been correctly categorize (training data). You decide to use Machine Learning on this data in order to categorize the uncategorized documents.

Training Data

In order to figure out what category each document should fall under you will base it on the categories of the documents in the "trainingdata.txt" file. This file will be included with your program at runtime and will be named "trainingdata.txt".

The file is formatted as follows:

The first line contains the number of lines that will follow.

Each following line will contain a number (1-8), which is the category number. The number will be followed by a space then some space seperated words which is the processed document.

Input

The first line in the input file will contain T the number of documents. T lines will follow each containing a series of space seperated words which represents the processed document.

Output

For each document output a number between 1-8 which you believe this document should be categorized as.

Sample Input

3
This is a document
this is another document
documents are seperated by newlines

Sample Output

1
4
8

Scoring

Your score for this challenge will be 100* (#correctly categorized - #incorrectly categorized)/(T).
