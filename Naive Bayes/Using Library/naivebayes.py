import numpy as np
from numpy import *
import pandas as pd
from sklearn.naive_bayes import MultinomialNB

data=loadtxt('train.data')
dataframe = pd.DataFrame(data, columns=['DocID', 'WordID', 'Freq'])
label=loadtxt('train.label')
labelframe = pd.DataFrame(label, columns=['label'])
labelframe['DocID']=labelframe.index+1
finaldata=pd.merge(dataframe,labelframe,on="DocID")
traindata=finaldata[['DocID','WordID']]

traindata_target=finaldata['label']
trainData_Target = traindata_target.as_matrix()

testdata=loadtxt('test.data')
Test_Data=pd.DataFrame(testdata, columns=['DocID', 'WordID', 'Freq'])
TestDatatest=Test_Data[['DocID','WordID']]

clf = MultinomialNB()
clf.fit(traindata,trainData_Target)

print(clf.predict(TestDatatest))
print "Naive Bayes accuracy is"
print clf.score(traindata, trainData_Target)