#!/bin/bash
# for ((COUNT = 1; COUNT <= 4; COUNT++)); do
#   cat ./test.txt | head -n $COUNT | tail -n 1
#   sleep 1
# done
while :
do
    cat ./test.txt ; echo
    sleep 25
done