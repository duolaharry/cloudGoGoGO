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
    # sc = SparkContext(appName="PythonStreamingHDFSWordCount", master="spark://192.168.0.110:7077")
    sc = SparkContext(appName="PythonStreamingHDFSWordCount")
    ssc = StreamingContext(sc, 30)

    # compute for people
    # lines = ssc.textFileStream("hdfs://192.168.0.110:9000/wcy1/tmp/")
    #people = sc.textFile("/home/pluviophile/Documents/tmp/people.txt")
    people = ssc.textFileStream("hdfs://192.168.0.110:9000/origin/people/")
    # counts = lines.flatMap(lambda line: line.split("\n")) \
    #     .map(lambda x: (x, 1)) \
    #     .reduceByKey(lambda a, b: a + b)
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
    popu = ssc.textFileStream("hdfs://192.168.0.110:9000/origin/popular/")
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
    meanByName.pprint()
    meanByName.repartition(1).saveAsTextFiles("hdfs://192.168.0.110:9000/11141559/output")
    # counts.foreachRDD(lambda rdd: rdd.saveAsTextFiles("hdfs://192.168.0.110:9000/wcy2/output"))

    ssc.start()
    ssc.awaitTermination()
