#/bin/bash
set -eu

if [ "$#" -eq 0  ] 
then
    # size=$(stat --format=%s $thing)
    # column --table --table-noheadings --table-columns $(ls), $(stat --format=%s | ls) #--table-right $(ls | stat --format=%s)
    for value in $(ls .); do
        size=$(echo | stat --format=%s $value)
        column -t --table-noheadings --table-columns "dirName","sizes" --table-right  "sizes" "dir.sh"
    done
    
else
    for thing in "$@"
    do
        stat --format=%s $thing
    done
fi
