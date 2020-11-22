from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext


def mapBynum(x):
    list1 = x.split(" ")[1].split(":")
    list2 = []
    list2.append("num")
    list2.append(int(list1[1]))
    return list2


def mapByName(x):
    list1 = x.split(" ")
    list2 = []
    list2.append("num")
    list2.append(int((list1[1].split(":"))[1]))
    return list2


if __name__ == "__main__":
    # 初始化本地变量
    sumOfPeople = 1
    sumOfPopular = 1

    # 设置流监听，监听源为hdfs文件系统
    sc = SparkContext(appName="PythonStreamingHDFSWordCount")
    ssc = StreamingContext(sc, 30)

    # 对直播人数rdd进行处理
    people = ssc.textFileStream("hdfs://wcy-pc:9000/origin/people/")
    peopleCounts = people.map(lambda x: (mapBynum(x)[0], mapBynum(x)[1])) \
        .reduceByKey(lambda a, b: a + b)

    # 为了数据分离，有利于后续数据处理，这里重新创建一个新的rdd
    peopleWithName = people.map(lambda x: (mapByName(x)[0], mapByName(x)[1])) \
        .reduceByKey(lambda a, b: a + b)

    # 对直播人气rdd进行处理。
    popu = ssc.textFileStream("hdfs://wcy-pc:9000/origin/popular/")
    popuCounts = popu.map(lambda x: (mapBynum(x)[0], mapBynum(x)[1])) \
        .reduceByKey(lambda a, b: a + b)

    # 为了数据分离，有利于后续数据处理，这里重新创建一个新的rdd
    popuWithName = popu.map(lambda x: (mapByName(x)[0], mapByName(x)[1])) \
        .reduceByKey(lambda a, b: a + b)

    # 计算每个直播间的平均热度
    peopleCounts.union(popuCounts).pprint()
    popularForEachRoom = peopleCounts.union(popuCounts).reduceByKey(lambda a, b: (0.0 + float(b)) / a)
    popularForEachRoom.pprint()
    # join by key
    # meanByName = popuWithName.join(peopleWithName)
    #
    # listOfRecord = []


    # def takeAndPrint1(time, rdd):
    #     taken = rdd.take(21)
    #     print("--------------------!-----------------------")
    #     print("Time: %s" % time)
    #     print("--------------------!-----------------------")
    #     for record in taken[:20]:
    #         listOfRecord.append(record)
    #     if len(taken) > 20:
    #         print("...")
    #     print("")
    #     print(listOfRecord)

    #meanByName.foreachRDD(takeAndPrint1)

    # 开始监听
    ssc.start()
    ssc.awaitTermination()
