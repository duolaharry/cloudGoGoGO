def dataPreprocessForHuya(fileDir):
    numOfPeople = []
    popularityOfChannnel = []
    file = open(fileDir, mode='r')
    data = file.read()
    dataSet = data.split("==")
    dataSet.pop(0)
    # print(dataSet[0])
    for dataSetPerTimeUnit in dataSet:
        subDataSet = dataSetPerTimeUnit.split("当前")
        lines = subDataSet[2].split("\n")
        lines.pop(0)
        for item in lines:
            if item.startswith("共"):
                tmpSet = {}
                tmpstr = item.split("共有")
                tmpstr = tmpstr[1].split("人直播")
                tmpnum = tmpstr[0]
                tmpstr = tmpstr[1].split(",比例为")
                tmpname = tmpstr[0]
                tmpratio = tmpstr[1]
                tmpSet["name"] = tmpname
                tmpSet["ratio"] = tmpratio
                tmpSet["num"] = tmpnum
                numOfPeople.append(tmpSet)
        lines = subDataSet[3].split("\n")
        lines.pop(0)
        for item in lines:
            if not item.startswith("-") and item != '':
                tmpSet = {}
                tmpstr = item.split(",")
                tmpname = tmpstr[1]
                tmpnum = tmpstr[2][3:]
                tmpratio = tmpstr[3][3:]
                tmpSet["name"] = tmpname
                tmpSet["ratio"] = tmpratio
                tmpSet["num"] = tmpnum
                popularityOfChannnel.append(tmpSet)
    print(numOfPeople)
    print(popularityOfChannnel)


def dataPreprocessForDouyu(fileDir):
    numOfPeople = []
    popularityOfChannnel = []
    file = open(fileDir, mode='r')
    data = file.read()
    dataSet = data.split("==")
    dataSet.pop(0)
    # print(dataSet[0])
    for dataSetPerTimeUnit in dataSet:
        subDataSet = dataSetPerTimeUnit.split("当前斗鱼")
        lines = subDataSet[3].split("当前共有")
        lines.pop(0)
        for item in lines:
            tmpSet = {}
            tmpstr = item.split("人正在直播【")
            tmpnum = tmpstr[0]
            tmpstr = tmpstr[1].split("】 - 占比:")
            tmpname = tmpstr[0]
            tmpratio = (tmpstr[1].split("\n"))[0]
            tmpSet["name"] = tmpname
            tmpSet["ratio"] = tmpratio
            tmpSet["num"] = tmpnum
            numOfPeople.append(tmpSet)
        lines = subDataSet[2].split("【")
        lines.pop(0)
        for item in lines:
            tmpSet = {}
            tmpstr = item.split("】 - 人气热度:")
            tmpname = tmpstr[0]
            tmpstr = tmpstr[1].split(" - 占比:")
            tmpnum = tmpstr[0]
            tmpratio = (tmpstr[1].split("\n"))[0]
            tmpSet["name"] = tmpname
            tmpSet["ratio"] = tmpratio
            tmpSet["num"] = tmpnum
            popularityOfChannnel.append(tmpSet)
    print(numOfPeople)
    print(popularityOfChannnel)


if __name__ == "__main__":
    sumOfPopular = 16
    sumOfPopular = 10
    result = (0.0 + sumOfPopular) / (sumOfPopular + 0.0)
    print(result)
    print(0.0 + 1)
    # dataPreprocessForHuya("/home/pluviophile/Documents/tmp/res.txt")
    # dataPreprocessForDouyu("/home/pluviophile/Documents/tmp/res2.txt")
