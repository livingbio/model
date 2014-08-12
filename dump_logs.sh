#!/bin/bash

echo "start dump log $1 to $2"


logs=`gsutil ls "gs://tagtooad-test/log2bq-$1*"`

pids=""
csvs=""


## download & format & sort log
for log in $logs; do
    echo "start download & format log $log"
    csv=`basename $log`.csv
    gsutil cat $log | ./log_format.py | sort > /tmp/$csv&
    csvs="$csvs $csv"
    pids="$pids $!"
done

echo $pids

for pid in $pids; do
    wait $pid
    echo "$pid is success"   
done



## csv log merge
echo "start merge"
cat $csvs | sort| ./log_merge.py > $2

echo "start remove csv file"
for csv in $csvs; do
    rm /tmp/$csv
done


#gsutil cat "gs://tagtooad-test/log2bq-$1*" | ./log_format.py | sort | ./log_merge.py > $2
