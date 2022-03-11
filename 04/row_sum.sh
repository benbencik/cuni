#!/bin/bash

res=()
sed -e '/^$/,$d' <<EOF

sed -e
while read -r line;
do
    res+=$line;
done

for r in $res
do
    echo $r
done