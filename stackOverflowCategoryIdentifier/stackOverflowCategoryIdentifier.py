# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import re
import collections
import json
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from time import time
from sklearn.pipeline import Pipeline

text_clf = Pipeline([('vect', CountVectorizer(stop_words='english', min_df=1, max_df=.85)),
                     ('tdf', TfidfTransformer()),
                      ('clf', MultinomialNB())])

regex = re.compile('[^a-zA-Z ]')


f = open('training.json', 'r')
t = int(f.readline())
data = []
for i in range(t):
    data.append(json.loads(f.readline()))

questions=map(lambda x: x['question'].encode('utf-8')+x['excerpt'].encode('utf-8'), data)
labels=map(lambda x: x['topic'].encode('utf-8'), data)
#t0=time()
text_clf.fit(questions, labels)
#print("time to fit: %.3f"% (time()-t0))

numToPredict = int(raw_input())
predict = []
for i in range(numToPredict):
    predict.append(json.loads(raw_input()))
encodedPredict = map(lambda x: x['question'].encode('utf-8'), predict)
print(''.join(x+'\n' for x in text_clf.predict(encodedPredict)))
