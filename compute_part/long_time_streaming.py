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
    # 设置流监听，监听源为hdfs文件系统
    sc = SparkContext(appName="PythonStreamingLongTime")
    ssc = StreamingContext(sc, 30)
    douyuPeople = ssc.textFileStream("hdfs://wcy-pc:9000/longtime/douyu/people/")
    douyuPopu = ssc.textFileStream("hdfs://wcy-pc:9000/longtime/douyu/popular/")
    huyaPeople = ssc.textFileStream("hdfs://wcy-pc:9000/longtime/huya/people/")
    huyaPopu = ssc.textFileStream("hdfs://wcy-pc:9000/longtime/huya/popular/")
    data = []  # 保存输出流

    # 对直播人数rdd进行处理
    douyuPeopleCounts = douyuPeople.map(lambda x: (mapBynum(x)[0], mapBynum(x)[1])) \
        .reduceByKey(lambda a, b: a + b)
    huyaPeopleCounts = huyaPeople.map(lambda x: (mapBynum(x)[0], mapBynum(x)[1])) \
        .reduceByKey(lambda a, b: a + b)


    def outputDouyuPeopleCounts(time, rdd):
        s = "Time: %s" % time
        print("-------------------------------------------")
        # print("outputpopuCounts Time: %s" % time)
        # print("-------------------------------------------")
        taken = rdd.take(1)
        if len(taken) > 0:
            record = taken[0]
            print(["斗鱼", "people", record[1]])
            item = "斗鱼 " + "people " + str(record[1])
            data.append(item)


    douyuPeopleCounts.repartition(1).foreachRDD(outputDouyuPeopleCounts)


    def outputHuyaPeopleCounts(time, rdd):
        s = "Time: %s" % time
        # print("-------------------------------------------")
        # print("outputpopuCounts Time: %s" % time)
        # print("-------------------------------------------")
        taken = rdd.take(1)
        if len(taken) > 0:
            record = taken[0]
            print(["虎牙", "people", record[1]])
            item = "虎牙 " + "people " + str(record[1])
            data.append(item)


    huyaPeopleCounts.repartition(1).foreachRDD(outputHuyaPeopleCounts)

    # 对直播人气rdd进行处理。
    douyuPopuCounts = douyuPopu.map(lambda x: (mapBynum(x)[0], mapBynum(x)[1])) \
        .reduceByKey(lambda a, b: a + b)
    huyaPopuCounts = huyaPopu.map(lambda x: (mapBynum(x)[0], mapBynum(x)[1])) \
        .reduceByKey(lambda a, b: a + b)


    def outputDouyuPopuCounts(time, rdd):
        s = "Time: %s" % time
        # print("-------------------------------------------")
        # print("outputpopuCounts Time: %s" % time)
        # print("-------------------------------------------")
        taken = rdd.take(1)
        if len(taken) > 0:
            record = taken[0]
            print(["斗鱼", "popu", record[1]])
            item = "斗鱼 " + "popu " + str(record[1])
            data.append(item)


    douyuPopuCounts.repartition(1).foreachRDD(outputDouyuPopuCounts)


    def outputHuyaPopuCounts(time, rdd):
        s = "Time: %s" % time
        # print("-------------------------------------------")
        # print("outputpopuCounts Time: %s" % time)
        # print("-------------------------------------------")
        taken = rdd.take(1)
        if len(taken) > 0:
            record = taken[0]
            print(["虎牙", "popu", record[1]])
            item = "虎牙 " + "popu " + str(record[1])
            data.append(item)


    huyaPopuCounts.repartition(1).foreachRDD(outputHuyaPopuCounts)

    # 对板块的直播人数rdd进行处理
    douyuPeopleCountsForeach = douyuPeople.map(lambda x: (mapByName(x)[0], mapByName(x)[1])) \
        .reduceByKey(lambda a, b: a + b)
    huyaPeopleCountsForeach = huyaPeople.map(lambda x: (mapByName(x)[0], mapByName(x)[1])) \
        .reduceByKey(lambda a, b: a + b)


    def outputDouyuPeopleCountsForeach(time, rdd):
        s = "Time: %s" % time
        # print("-------------------------------------------")
        # print("outputpopuCounts Time: %s" % time)
        # print("-------------------------------------------")
        taken = rdd.take(21)
        if len(taken) > 0:
            for record in taken[:20]:
                print(["斗鱼", "people", record[0], record[1]])
                item = "斗鱼 " + "people " + record[0] + " " + str(record[1])
                data.append(item)


    douyuPeopleCountsForeach.repartition(1).foreachRDD(outputDouyuPeopleCountsForeach)


    def outputHuyaPeopleCountsForeach(time, rdd):
        s = "Time: %s" % time
        # print("-------------------------------------------")
        # print("outputpopuCounts Time: %s" % time)
        # print("-------------------------------------------")
        taken = rdd.take(21)
        if len(taken) > 0:
            for record in taken[:20]:
                print(["虎牙", "people", record[0], record[1]])
                item = "虎牙 " + "people " + record[0] + " " + str(record[1])
                data.append(item)


    huyaPeopleCountsForeach.repartition(1).foreachRDD(outputHuyaPeopleCountsForeach)

    # 对板块的直播人气rdd进行处理。
    douyuPopuCountsForeach = douyuPopu.map(lambda x: (mapByName(x)[0], mapByName(x)[1])) \
        .reduceByKey(lambda a, b: a + b)
    huyaPopuCountsForeach = huyaPopu.map(lambda x: (mapByName(x)[0], mapByName(x)[1])) \
        .reduceByKey(lambda a, b: a + b)


    def outputDouyuPopuCountsForeach(time, rdd):
        s = "Time: %s" % time
        # print("-------------------------------------------")
        # print("outputpopuCounts Time: %s" % time)
        # print("-------------------------------------------")
        taken = rdd.take(21)
        if len(taken) > 0:
            for record in taken[:20]:
                print(["斗鱼", "popu", record[0], record[1]])
                item = "斗鱼 " + "popu " + record[0] + " " + str(record[1])
                data.append(item)


    douyuPopuCountsForeach.repartition(1).foreachRDD(outputDouyuPopuCountsForeach)


    def outputHuyaPopuCountsForeach(time, rdd):
        s = "Time: %s" % time
        # print("-------------------------------------------")
        # print("outputpopuCounts Time: %s" % time)
        # print("-------------------------------------------")
        taken = rdd.take(21)
        if len(taken) > 0:

            for record in taken[:20]:
                print(["虎牙", "popu", record[0], record[1]])
                item = "虎牙 " + "popu " + record[0] + " " + str(record[1])
                data.append(item)
            file = open("/home/pluviophile/Documents/tmp/longtime/output1/longOutput.txt", "w", encoding='utf-8')
            for i in data:
                file.write(i + "\n")
            file.close()
            data.clear()

    huyaPopuCountsForeach.repartition(1).foreachRDD(outputHuyaPopuCountsForeach)

    # 开始监听
    ssc.start()
    ssc.awaitTermination()
