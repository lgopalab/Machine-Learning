from sklearn import cross_validation
import sys
import numpy
import pandas
import math
from sklearn import svm


data=pandas.read_csv("D:/Courses_Fall2016/MachineLearning/ITCS6156_HW1/ITCS6156_HW1/20news-bydate/data/train.data", header=None, sep=" ", names=["d", "w", "f"])
labels=pandas.read_csv("D:/Courses_Fall2016/MachineLearning/ITCS6156_HW1/ITCS6156_HW1/20news-bydate/data/train.label", header=None, names=["label"])
labels.index=labels.index+1
labels['d']=labels.index

data=pandas.merge(data, labels, on="d")

a=list(data.columns[:1])
y=data['label']
x=data[a]

X_train, X_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.4, random_state=0)
classifier = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
classifier.score(X_test, y_test)



