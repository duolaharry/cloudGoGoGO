from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext


def mapBynum(x):
    list1 = x.split(" ")[1].split(":")
    list2 = ["num", int(list1[1])]
    return list2


def mapByName(x):
    list1 = x.split(" ")
    list2 = [(list1[0].split(":"))[1], int((list1[1].split(":"))[1])]
    return list2


if __name__ == "__main__":
    # 初始化本地变量
    historyOfPeopleEachName = []  # 存放people历史板块数据
    currentPeopleEachName = []  # 存放people当前板块数据
    historyOfPopuEachName = []  # 存放popu历史板块数据
    currentPopuEachName = []  # 存放popu当前板块数据
    calculateChangePeopleDateList = []  # 存放变化people计算数据
    calculateChangePopuDateList = []  # 存放变化popu计算数据
    data = []  # 保存输出流

    # 设置流监听，监听源为hdfs文件系统
    sc = SparkContext(appName="PythonStreamingShortTime")
    ssc = StreamingContext(sc, 30)
    people = ssc.textFileStream("hdfs://wcy-pc:9000/origin/people/")
    popu = ssc.textFileStream("hdfs://wcy-pc:9000/origin/popular/")

    # 对直播人数rdd进行处理
    peopleCounts = people.map(lambda x: (mapBynum(x)[0], mapBynum(x)[1])) \
        .reduceByKey(lambda a, b: a + b)


    def outputpeopleCounts(time, rdd):
        print("-------------------------------------------")
        print("outputpeopleCounts Time: %s" % time)
        print("-------------------------------------------")
        taken = rdd.take(1)
        if len(taken) > 0:
            record = taken[0]
            print(["allpeople", "people", record[1]])
            item = "allPeople " + "people " + str(record[1])
            data.append(item)


    peopleCounts.repartition(1).foreachRDD(outputpeopleCounts)

    # 对直播人气rdd进行处理。
    popuCounts = popu.map(lambda x: (mapBynum(x)[0], mapBynum(x)[1])) \
        .reduceByKey(lambda a, b: a + b)


    def outputpopuCounts(time, rdd):
        print("-------------------------------------------")
        print("outputpopuCounts Time: %s" % time)
        print("-------------------------------------------")
        taken = rdd.take(1)
        if len(taken) > 0:
            record = taken[0]
            print(["allpopu", "popu", record[1]])
            item = "allPopu " + "popu " + str(record[1])
            data.append(item)


    popuCounts.repartition(1).foreachRDD(outputpopuCounts)

    # 计算每个直播间的平均热度
    popularForEachRoom = peopleCounts.union(popuCounts).reduceByKey(lambda a, b: (0.0 + float(b)) / a)


    def calculateForMean(time, rdd):
        print("-------------------------------------------")
        print("calculateForMean Time: %s" % time)
        print("-------------------------------------------")
        taken = rdd.take(1)
        if len(taken) > 0:
            record = taken[0]
            print(["allmean", record[1]])
            item = "allMean " + str(record[1])
            data.append(item)


    popularForEachRoom.repartition(1).foreachRDD(calculateForMean)

    # 计算各个板块人数的变更情况
    peopleChange = people.map(lambda x: (mapByName(x)[0], mapByName(x)[1])) \
        .reduceByKey(lambda a, b: a + b)


    def calculateForPeopleChange(time, rdd):
        print("-------------------------------------------")
        print("calculateForPeopleChange Time: %s" % time)
        print("-------------------------------------------")
        taken = rdd.take(21)
        currentPeopleEachName = []
        calculateChangePeopleDateList = []
        tmpHistoryName = []
        tmpCurrntName = []
        for record in taken[:20]:
            currentPeopleEachName.append(record)
            tmpCurrntName.append(record[0])
        if len(historyOfPeopleEachName) == 0:
            for record in currentPeopleEachName:
                historyOfPeopleEachName.append(record)
        for i in historyOfPeopleEachName:
            tmpHistoryName.append(i[0])
        for i in range(0, len(currentPeopleEachName)):
            if currentPeopleEachName[i][0] in tmpHistoryName:
                for j in range(0, len(historyOfPeopleEachName)):
                    if currentPeopleEachName[i][0] == historyOfPeopleEachName[j][0]:
                        tmplist = [currentPeopleEachName[i][0],
                                   int(currentPeopleEachName[i][1]) - int(historyOfPeopleEachName[j][1])]
                        calculateChangePeopleDateList.append(tmplist)
            else:
                tmplist = [currentPeopleEachName[i][0], int(currentPeopleEachName[i][1])]
                calculateChangePeopleDateList.append(tmplist)
        for i in range(0, len(historyOfPeopleEachName)):
            if historyOfPeopleEachName[i][0] not in tmpCurrntName:
                tmplist = [historyOfPeopleEachName[i][0], 0 - int(historyOfPeopleEachName[i][1])]
                calculateChangePeopleDateList.append(tmplist)
        historyOfPeopleEachName.clear()
        for record in currentPeopleEachName:
            historyOfPeopleEachName.append(record)
        print(calculateChangePeopleDateList)
        for record in calculateChangePeopleDateList:
            item = "peopleChange " + str(record[0]) + " " + str(record[1])
            data.append(item)


    peopleChange.repartition(1).foreachRDD(calculateForPeopleChange)

    # 计算各个板块人气的变更情况
    popuChange = popu.map(lambda x: (mapByName(x)[0], mapByName(x)[1])) \
        .reduceByKey(lambda a, b: a + b)


    def calculateForPopuChange(time, rdd):
        print("-------------------------------------------")
        print("calculateForPopuChange Time: %s" % time)
        print("-------------------------------------------")
        taken = rdd.take(20)
        currentPopuEachName = []
        calculateChangePopuDateList = []
        tmpHistoryName = []
        tmpCurrntName = []
        for record in taken[:19]:
            currentPopuEachName.append(record)
            tmpCurrntName.append(record[0])
        if len(historyOfPopuEachName) == 0:
            for record in currentPopuEachName:
                historyOfPopuEachName.append(record)
        for i in historyOfPopuEachName:
            tmpHistoryName.append(i[0])
        for i in range(0, len(currentPopuEachName)):
            if currentPopuEachName[i][0] in tmpHistoryName:
                for j in range(0, len(historyOfPopuEachName)):
                    if currentPopuEachName[i][0] == historyOfPopuEachName[j][0]:
                        tmplist = [currentPopuEachName[i][0],
                                   int(currentPopuEachName[i][1]) - int(historyOfPopuEachName[j][1])]
                        calculateChangePopuDateList.append(tmplist)
            else:
                tmplist = [currentPopuEachName[i][0], int(currentPopuEachName[i][1])]
                calculateChangePopuDateList.append(tmplist)
        for i in range(0, len(historyOfPopuEachName)):
            if historyOfPopuEachName[i][0] not in tmpCurrntName:
                tmplist = [historyOfPopuEachName[i][0], 0 - int(historyOfPopuEachName[i][1])]
                calculateChangePopuDateList.append(tmplist)
        historyOfPopuEachName.clear()
        for record in currentPopuEachName:
            historyOfPopuEachName.append(record)
        print(calculateChangePopuDateList)
        for record in calculateChangePopuDateList:
            item = "popuChange " + str(record[0]) + " " + str(record[1])
            data.append(item)
        # [("PopuChange",record[0],record[1])]


    popuChange.repartition(1).foreachRDD(calculateForPopuChange)

    # 计算各个板块每个直播间的平均热度
    # 为了数据分离，有利于后续数据处理，这里重新创建一个新的rdd
    peopleWithName = people.map(lambda x: (mapByName(x)[0], mapByName(x)[1])) \
        .reduceByKey(lambda a, b: a + b)
    popuWithName = popu.map(lambda x: (mapByName(x)[0], mapByName(x)[1])) \
        .reduceByKey(lambda a, b: a + b)
    meanByName = popuWithName.join(peopleWithName)


    def calculateForNameMean(time, rdd):
        print("-------------------------------------------")
        print("calculateForNameMean Time: %s" % time)
        print("-------------------------------------------")
        taken = rdd.take(20)
        nameMeanList = []
        for record in taken[:19]:
            tmplist = [record[0], (0.0 + record[1][0]) / record[1][1]]
            nameMeanList.append(tmplist)
        print(nameMeanList)
        for record in nameMeanList:
            item = "nameMean " + str(record[0]) + " " + str(record[1])
            data.append(item)
        # [("nameMean",record[0],record[1])]
        file = open("/home/pluviophile/Documents/tmp/longtime/output1/shortOutput.txt", "w", encoding='utf-8')
        for i in data:
            file.write(i + "\n")
        file.close()
        data.clear()

    meanByName.repartition(1).foreachRDD(calculateForNameMean)

    # 开始监听
    ssc.start()
    ssc.awaitTermination()
