import numpy as np
import re
import collections
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from time import time
from sklearn.pipeline import Pipeline
import json
import sys
import io

text_clf = Pipeline([('vect', CountVectorizer()),
                      ('clf', MultinomialNB())])

regex = re.compile('[^a-zA-Z ]')

lines = []
f = open('training.json', 'r', encoding="utf-8")

t = int(f.readline())

docs = []
labels = []
for i in range(t):
    line=json.loads(f.readline())
    label=line['category']
    docs.append(line['heading'])
    labels.append(label)

t0 = time()
text_clf.fit(docs, labels)
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
toPredict = int(input_stream.readline())
predict=[]
for i in range(toPredict):
    predict.append(json.loads(input_stream.readline().strip())['heading'])

predictions=text_clf.predict(predict)
answer=str('').join(str(x)+'\n' for x in predictions)
print(answer.strip())
