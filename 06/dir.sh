#/bin/bash
set -eu

temp_dir="$( mktemp -d )"
table_info="$temp_dir/info"

list_info(){
    # if test -d $1 | test -f $1; then
        if test -d $1; then
            size="<dir>"
        elif test -f $1; then
            size=$(echo | stat --format=%s $1)
        else
            size="<special>"
        fi
        echo > /dev/null "$1 $size" >> $temp_dir/info
    # else
    #     echo 2> "$1: no such file or directory"
    # fi 
}
    

if [ "$#" -eq 0 ]; then
    for thing in *; do
        list_info $thing
    done
else
    for thing in "$@"; do
        list_info $thing
    done
fi


column $temp_dir/info -t -s ' ' --table-noheadings --table-right 2