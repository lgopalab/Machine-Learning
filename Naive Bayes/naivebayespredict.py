def naivebayespredict(data,model):
    probtable = {}
    lines = data.readlines()
    filewords = {}
    temp = {}

    for i in range(len(lines)):
        temp[i] = lines[i].split()

    filewordfreq = collections.defaultdict(dict)

    for i in range(len(temp)):
        filewordfreq[temp[i][0]][temp[i][1]]=temp[i][2]

    for i in range(len(temp)):
        print filewordfreq[temp[i][0]].keys()
