#!/bin/bash
set -eu

temp_dir="$( mktemp -d )"

list_info(){
    size=''
    if test -e "$1"; then
        if test -d "$1"; then
            size="<dir>"
        elif test -f "$1"; then
            size=$(echo | stat --format=%s "$1")
        else
            # if test -b $1; then
            size="<special>"
            # fi

        fi

        if [ $size != '' ]; then
            echo > /dev/null "$1 $size"
        fi
    else
        >&2 echo "$1: no such file or directory."
    fi 
}
    

if [ "$#" -eq 0 ]; then
    # itterate over current directory
    if [ "" != "$(ls)" ]; then
        for thing in *; do
            list_info "$thing"
        done
    fi
else
    # itterate over argumetns provided
    for thing in "$@"; do
        list_info "$thing"
    done
fi


if test -e "$temp_dir"/info; then
    column "$temp_dir"/info -t -s ' ' --table-noheadings --table-right 2
fi