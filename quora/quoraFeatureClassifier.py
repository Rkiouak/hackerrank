import numpy as np
import re
import collections
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
from time import time
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import normalize
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn import neighbors
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, ExtraTreesClassifier, AdaBoostClassifier
from sklearn.svm import LinearSVC

#param_grid=[{'criterion':['gini'], 'splitter':['best'], 'max_depth':[5]}]
#param_grid=[{'n_neighbors':[5,10,15], 'weights':['uniform', 'distance'], 'algorithm':['auto', 'ball_tree', 'kd_tree']}]
#param_grid=[{'n_estimators':[3,5,10], 'max_features':['auto', 5, .75, 'log2'], 'class_weight':['balanced', 'balanced_subsample']}]

text_clf = Pipeline([#('tdf', TfidfTransformer()),
                      #('clf', ExtraTreesClassifier(n_estimators=200, max_depth=None,
     #min_samples_split=2, random_state=69))
                       ('clf', AdaBoostClassifier(n_estimators=150))])

#text_clf = GridSearchCV(neighbors.KNeighborsClassifier(), param_grid)

lines = []

t = int(input().split(' ')[0])

docs = []
labels = []
for i in range(t):
    line=input().split(' ')
    label=int(line[1])
    docs.append(list(map(lambda x: float(x.split(':')[1]), line[2:])))
    labels.append(label)


t0 = time()
#print(docs)
#print(labels)
text_clf.fit(docs, labels)
#print('%.3f'%(time()-t0))

toPredict = int(input())
predict=[]
predictKey=[]
for i in range(toPredict):
    line = input().split(' ')
    predict.append(list(map(lambda x: float(x.split(':')[1]), line[1:])))
    predictKey.append(line[0])

predictions=text_clf.predict(predict)
answer=''
for i in range(len(predictions)):
    answer+=str(predictKey[i])+' '+str(predictions[i])+'\n' if predictions[i]<0 else str(predictKey[i])+' +'+str(predictions[i])+'\n'
print(answer.strip())
