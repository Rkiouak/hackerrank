import numpy as np
import re
import collections
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from time import time
from sklearn.pipeline import Pipeline

text_clf = Pipeline([('vect', CountVectorizer()),
                      ('clf', MultinomialNB())])

regex = re.compile('[^a-zA-Z ]')

lines = []
f = open('trainingdata.txt', 'r')

t = int(f.readline())

docs = []
labels = []
corpus = set()
for i in range(t):
    line=f.readline()
    label=line[0]
    docs.append(line[2:])
    labels.append(label)

t0 = time()
text_clf.fit(docs, labels)

toPredict = int(input())
predict=[]
for i in range(toPredict):
    predict.append(input().strip())

predictions=text_clf.predict(predict)
answer=str('').join(str(x)+'\n' for x in predictions)
print(answer.strip())
