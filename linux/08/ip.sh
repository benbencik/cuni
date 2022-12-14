#!/bin/bash
set -ueo pipefail

temp_dir="$( mktemp -d )"
machine=''
max_attempts=0


while read -r ip; do
# for ip in $(grep -E "404" | cut -d ' ' -f 1); do
    # ip="$(grep -E "404" | cut -d ' ' -f 1)"
    # echo $ip
    if test -f "$temp_dir/$ip"; then
        current="$(cat "$temp_dir/$ip")"
        current=$((current + 1))
        echo $current > "$temp_dir/$ip"  
    else
        echo 1 > "$temp_dir/$ip"
    fi

    if [ "$(cat "$temp_dir/$ip")" -gt $max_attempts ]; then
        max_attempts=$(cat "$temp_dir/$ip")
        machine=$ip
    fi
done < <(grep -E "404" | cut -d ' ' -f 1)

echo "$machine"