import collections
from naivebayespredict import naivebayespredict

def naivebayestrain(data,labels,alpha):
    labelline = labels.readlines()
    dataline = data.readlines()
    str = ""

    for i in dataline:
        temp = i.split()
        str += labelline[int(temp[0])-1].replace("\n","") +" "+ temp[1]+" "+temp[2] +"\n"

    text_file = open("train.txt", "w")
    text_file.write(str)
    text_file.close()

    worddict = {}
    catexample = {}
    wordprob = {}
    parseddata = open('train.txt')
    parseddataline = parseddata.readlines()
    for i in parseddataline:
        temp = i.split()
        worddict[temp[0], temp[1]] = 0
        catexample[temp[0]] = 0

    for i in parseddataline:
        temp = i.split()
        catexample[temp[0].strip()] = catexample[temp[0].strip()] + 1
        if worddict[temp[0], temp[1]] == 0:
            worddict[temp[0], temp[1]] = int(temp[2])
        else:
            worddict[temp[0], temp[1]] += int(temp[2])

    for i in worddict:
        wordprob[i[0], i[1]] = float(int(worddict[i[0], i[1]]) + alpha) / (int(catexample[i[0]]) + 2 * alpha)

    return wordprob



def categorycount(pivot):
    labels = open('src/20news/data/train.label')
    map = open('src/20news/data/train.map')
    maplist = map.readlines()
    mapdict = {}
    for i in maplist:
        linesplit = i.split()
        mapdict[linesplit[1]]=linesplit[0]

    #for i in sorted(mapdict.iterkeys()):
        #print mapdict[i]

    labelslist = labels.readlines()
    labelslistint = []
    labelslistcount = {}

    for i in labelslist:
        labelslistint.append(i.strip())

    for i in range(len(mapdict.keys())):
        labelslistcount[i+1] = labelslistint.count(str(i+1))

    return float(labelslistcount[pivot])/float(sum(labelslistcount.values()))



def main():
    data = open('src/20news/data/train.data')
    data2 = open('test.txt')
    labels = open('src/20news/data/train.label')
    labels2 = open('src/20news/data/test.label')

    alpha = 1
    model = naivebayestrain(data,labels,alpha)

    for key in sorted(model)[:50]:
        print key, model[key]
    #naivebayespredict(data2, model)
    #categorycount(2)
    #print model['20', '19590']


if __name__ == "__main__":
    main()

