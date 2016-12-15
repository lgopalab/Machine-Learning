import numpy as np
from numpy import *
import pandas as pd
import math

def entropy():
	uniquelabel=np.unique(finaldata['ClassLabel'])
	entropy=0
	for label in uniquelabel:
		uniquelabel_count=finaldata[finaldata['ClassLabel']==label]
		labelcount=len(uniquelabel_count.index)
		value=float(labelcount)/float(data_length)
		entropy=entropy+value*(math.log(value,2))
	return entropy

def feature_entropy(feature):
	entropyvalue_feature=0.0
	IDs=np.unique(finaldata[feature])
	for id in IDs:
		data=finaldata[finaldata[feature]==id]
		id_count=len(data.index)
		x=float(id_count)/float(data_length)
		uniquelabel=np.unique(data['ClassLabel'])
		labelcount=data['ClassLabel'].value_counts()
		y=0.0
		for label in uniquelabel:
			label_dataframe=data[data['ClassLabel']==label]
			label_count=len(label_dataframe.index)
			xi=float(label_count)/float(id_count)
			y=y+xi*(math.log(xi,2))
		entropyvalue_feature=entropyvalue_feature+x*y
	return entropyvalue_feature

def InformationGain(feature):
	return abs(entropy())-feature_entropy(feature)

traindata=loadtxt('D:/Classes/Fall 2016/Machine Learning/HW1/src/20news/data/train.data')
dataframe = pd.DataFrame(traindata, columns=['DocID', 'WordID', 'Freq'])

classlabel=loadtxt('D:/Classes/Fall 2016/Machine Learning/HW1/src/20news/data/train.label')
labelframe = pd.DataFrame(classlabel, columns=['ClassLabel'])
labelframe['DocID']=labelframe.index+1

testdata=loadtxt('D:/Classes/Fall 2016/Machine Learning/HW1/src/20news/data/test.data')
testdata=pd.DataFrame(testdata, columns=['DocID', 'WordID', 'Freq'])

finaldata=pd.merge(dataframe,labelframe,on="DocID")

traindata=finaldata[['DocID','WordID']]
traindata_target=finaldata['ClassLabel']
data_length=len(finaldata.index)

InformationGainVector=[]
Datafeatures=['DocID','WordID']
	
for feature in Datafeatures:
	InformationGainVector.append(InformationGain(feature))

print InformationGainVector