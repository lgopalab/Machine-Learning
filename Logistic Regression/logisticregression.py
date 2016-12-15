import sys
import numpy
import pandas
import math
from sklearn.linear_model import LogisticRegression

train=pandas.read_csv("D:\Classes\Fall 2016\Machine Learning\HW2\data/train.data", header=None, sep=" ", names=['DocID', 'WordID', 'Freq'])
labelstrain=pandas.read_csv("D:\Classes\Fall 2016\Machine Learning\HW2\data/train.label", header=None, names=["label"])
labelstrain.index=labelstrain.index+1
labelstrain['DocID']=labelstrain.index
train=pandas.merge(train, labelstrain, on="DocID")

test=pandas.read_csv("D:\Classes\Fall 2016\Machine Learning\HW2\data/test.data", header=None, sep=" ", names=['DocID', 'WordID', 'Freq'])
labelstest=pandas.read_csv("D:\Classes\Fall 2016\Machine Learning\HW2\data/test.label", header=None, names=["label"])
labelstest.index=labelstest.index+1
labelstest['DocID']=labelstest.index
test=pandas.merge(test, labelstest, on="DocID")

features=list(train.columns[:2])
y=train['label']
x=train[features]

testfeatures=list(test.columns[:2])
k=test[testfeatures]

def LRC(a,b,c):
 logistic = LogisticRegression()
 logistic.fit(a,b)
 predicted=logistic.predict(c)
 print "Logistic Regression accuracy is"
 print logistic.score(a,b)
 print predicted

LRC(x,y,k)



 