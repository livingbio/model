#!/bin/bash

## change temp path 
tmp="/ext-disk/"
export TMPDIR=$tmp


echo "start dump log $1 to $2"


logs=`gsutil ls "gs://tagtooad-test/log2bq-$1*"`

pids=""
csvs=""


ps=10
if [ $3 ]; then
    ps=$3
fi


## download & format & sort log
c=0
for log in $logs; do
    echo "start download & format log $log"
    name=`basename $log`
    gsutil cp $log $tmp$name
    echo "$log download success"
    cat $tmp$name | ./log_format.py | sort > $tmp${name}.csv&
    csvs="$csvs $tmp${name}.csv"
    pids="$pids $!"

    c=$(($c+1))
    if [ $c -ge $ps ] ; then 
        for pid in $pids; do
            wait $pid
            echo "$pid is success"   
        done
        pids=""
        c=0
    fi

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
    rm $csv
done

echo "start remove log file"
for log in $logs; do
    rm $tmp`basename ${log}`
done


#gsutil cat "gs://tagtooad-test/log2bq-$1*" | ./log_format.py | sort | ./log_merge.py > $2
