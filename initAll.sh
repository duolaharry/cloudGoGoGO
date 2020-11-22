#!/bin/bash

spark="/usr/lib/spark-3.0.1-bin-hadoop2.7/sbin"

$spark/stop-all.sh
$spark/start-master.sh
$spark/start-slaves.sh
