import sys
import numpy
import pandas
import math
from sklearn.tree import DecisionTreeClassifier

data=pandas.read_csv("D:/Classes/Fall 2016/Machine Learning/HW1/src/20news/data/train.data", header=None, sep=" ", names=["d", "w", "f"])
labels=pandas.read_csv("D:/Classes/Fall 2016/Machine Learning/HW1/src/20news/data/train.label", header=None, names=["label"])
labels.index=labels.index+1
labels['d']=labels.index

data=pandas.merge(data, labels, on="d")

a=list(data.columns[:1])
y=data['label']
x=data[a]

clf = DecisionTreeClassifier(min_samples_split=20, random_state=99)

classifier=clf.fit(x,y)

testdata=pandas.read_csv("D:/Classes/Fall 2016/Machine Learning/HW1/src/20news/data/test.data", header=None, sep=" ", names=["d", "w", "f"])
testlabels=pandas.read_csv("D:/Classes/Fall 2016/Machine Learning/HW1/src/20news/data/test.label", header=None, names=["label"])
testlabels.index=testlabels.index+1
testlabels['d']=testlabels.index

testdata=pandas.merge(testdata, labels, on="d")

test=list(testdata.columns[:1])
y=testdata['label']
x=testdata[test]

test=classifier.predict(2)

print classifier.score(x,y)
print(test)

