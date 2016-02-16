import numpy as np
import re
import collections
from sklearn.svm import SVC

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
    words=regex.sub('', line[1:]).split()
    words.sort()
    wordOccurences= dict()
    for word in words:
        corpus.add(word)
        if wordOccurences.get(word)==None:
            wordOccurences[word]=1
        else:
            wordOccurences[word]+=1    
    docs.append(wordOccurences)
    labels.append(label)

corpus=sorted(corpus)

trainingData = []
print(len(docs))
for occs in docs:
    docData=[]
    for word in corpus:
        docData.append(occs[word] if occs.get(word)!=None else 0)
    trainingData.append(docData)

clf = SVC()
clf.fit(trainingData, labels) 
#SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#    decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
#    max_iter=-1, probability=False, random_state=None, shrinking=True,
#    tol=0.001, verbose=False)
#print(clf.predict(trainingData))
