#!/bin/bash

hdfs="${HADOOP_HOME}/bin/hdfs dfs"

$hdfs -rm -r /longtime/douyu/people/
$hdfs -rm -r /longtime/douyu/popular/
$hdfs -mkdir  /longtime/douyu/people/
$hdfs -mkdir  /longtime/douyu/popular/
$hdfs -rm -r /longtime/huya/people/
$hdfs -rm -r /longtime/huya/popular/
$hdfs -mkdir  /longtime/huya/people/
$hdfs -mkdir  /longtime/huya/popular/

while [ 1 ] 
do
	tmp1="people`date +'%s'`.txt"
	tmp2="popular`date +'%s'`.txt"
	$hdfs -put -f ./Long/douyu/people.txt /longtime/douyu/people/$tmp1
	$hdfs -put -f ./Long/douyu/popular.txt /longtime/douyu/popular/$tmp2
	$hdfs -put -f ./Long/huya/people.txt /longtime/huya/people/$tmp1
	$hdfs -put -f ./Long/huya/popular.txt /longtime/huya/popular/$tmp2
	sleep 80
done
