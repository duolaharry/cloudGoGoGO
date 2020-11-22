from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":

    # 设置流监听，监听源为hdfs文件系统
    sc = SparkContext(appName="PythonStreamingLongTime")
    ssc = StreamingContext(sc, 30)