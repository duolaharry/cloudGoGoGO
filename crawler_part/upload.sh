#!/bin/bash

hdfs="${HADOOP_HOME}/bin/hdfs dfs"

$hdfs -rm -r /origin/people/
$hdfs -rm -r /origin/popular/
$hdfs -mkdir  /origin/people/
$hdfs -mkdir  /origin/popular/

while [ 1 ] 
do
	tmp1="people`date +'%s'`.txt"
	tmp2="popular`date +'%s'`.txt"
	$hdfs -put -f ./short/people.txt /origin/people/$tmp1
	$hdfs -put -f ./short/popular.txt /origin/popular/$tmp2
	sleep 85
done
