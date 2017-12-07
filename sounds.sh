#!/bin/bash

for i in `seq 1 106`;
do
    curl -X GET http://172.22.129.15:5000/aicar/test/06-$i-24
    sleep 1
done
