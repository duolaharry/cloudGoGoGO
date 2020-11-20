from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext


def mapBynum(x):
    list1 = x.split(" ")[1].split(":")
    list2 = []
    list2.append(list1[0])
    list2.append(int(list1[1]))
    return list2


def mapByName(x):
    list1 = x.split(" ")
    list2 = []
    list2.append((list1[0].split(":"))[1])
    list2.append(int((list1[1].split(":"))[1]))
    return list2

if __name__ == "__main__":
    sumOfPeople = 1
    sumOfPopular = 1
    sc = SparkContext(appName="PythonStreamingHDFSWordCount")
    ssc = StreamingContext(sc, 30)
    people = ssc.textFileStream("hdfs://wcy-pc:9000/origin/people/")
    peopleCounts = people.map(lambda x: (mapBynum(x)[0], mapBynum(x)[1])) \
        .reduceByKey(lambda a, b: a + b)
    peopleCounts.pprint()

    peopleWithName = people.map(lambda x: (mapByName(x)[0], mapByName(x)[1])) \
        .reduceByKey(lambda a, b: a + b)
    # output = peopleCounts.collect()
    # for a in output:
    #     sumOfPeople = a[1]

    # compute for popular
    # popu = sc.textFile("/home/pluviophile/Documents/tmp/popular.txt")
    popu = ssc.textFileStream("hdfs://wcy-pc:9000/origin/popular/")
    popuCounts = popu.map(lambda x: (mapBynum(x)[0], mapBynum(x)[1])) \
        .reduceByKey(lambda a, b: a + b)
    popuCounts.pprint()

    popuWithName = popu.map(lambda x: (mapByName(x)[0], mapByName(x)[1])) \
        .reduceByKey(lambda a, b: a + b)
    # output = popuCounts.collect()
    # for a in output:
    #     sumOfPopular = a[1]

    result = (0.0 + float(sumOfPopular)) / sumOfPeople

    # join by key

    meanByName = popuWithName.join(peopleWithName)
    # output = meanByName.collect()
    # for a in output:
    #     print(a)
    #     print(a[0])
    #     print(a[1])
    # meanByName.pprint()
    listOfRecord = []
    def takeAndPrint1(time, rdd):
        taken = rdd.take(21)
        print("--------------------!-----------------------")
        print("Time: %s" % time)
        print("--------------------!-----------------------")
        for record in taken[:20]:
            listOfRecord.append(record)
        if len(taken) > 20:
            print("...")
        print("")
        print(listOfRecord)
    # meanByName.repartition(1).saveAsTextFiles("hdfs://192.168.0.110:9000/11141559/output")
    meanByName.foreachRDD(takeAndPrint1)
    # counts.foreachRDD(lambda rdd: rdd.saveAsTextFiles("hdfs://192.168.0.110:9000/wcy2/output"))

    ssc.start()
    ssc.awaitTermination()

