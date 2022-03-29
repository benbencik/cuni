#!/bin/bash
set -ueo pipefail

temp_dir="$( mktemp -d )"
is_recorded=0

# calculate the final results 
while read -r scores; do
    is_recorded=0
    team=$( echo "$scores" | tr --squeeze-repeats ' ' | cut -d ' ' -f 1)
    score=$( echo "$scores" | tr --squeeze-repeats ' ' | cut -d ' ' -f 2)

    if $(test -f "$temp_dir/$team"); then
        current="$(cat "$temp_dir/$team")"
        current=$((current + score))
        echo $current > "$temp_dir/$team"  
    else
        echo $score > "$temp_dir/$team"
    fi
done

# print results
for team in $temp_dir/*; do
    value="$(cat $team)"
    team_name="$(echo $team | rev | cut -d '/' -f 1 | rev)"
    echo "$team_name:$value"
done

