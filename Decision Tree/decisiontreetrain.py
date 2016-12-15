from sklearn import tree

def decisionTreeTrain():

 classifier = tree.DecisionTreeClassifier()
 trainingset = open('train.txt')
 left = []
 right = []
 for i in trainingset:
    trainsplit=i.split()
    left.append([trainsplit[1],trainsplit[2]])
    right.append([trainsplit[3]])
 classifier = classifier.fit(left,right)

 testset = open('test.data')
 testparam = []
 testcat = []
 for j in testset:
    testsplit=j.split()
    testParam.append([[testsplit[1],testsplit[2]]])
    testCat.append(classifier.predict([[testsplit[1],testsplit[2]]]))
    print(classifier.predict([[testsplit[1],testsplit[2]]]))

def makefile():
    data = open('train.data')
    labels = open('train.label')
    map = open('train.map')
    mapline = map.readlines()
    labelline = labels.readlines()

    file = open('train.txt', 'w+')
    count = 0
    for i in data:
        array = i.split(' ')
        i = array[0]+' '+array[1]+ ' '+array[2]+ ' '+mapline[int(labelline[int(array[0])- 1])- 1].strip()
        i = i.replace('\n', '')
        count = count + 1
        file.write(i)
        file.write("\n")

def main():
    makefile()
    decisionTreeTrain()

if __name__ == "__main__":
    main()

