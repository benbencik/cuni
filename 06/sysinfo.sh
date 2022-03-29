#!/bin/bash
set -ueo pipefail

load="$(cat /proc/loadavg | cut -d ' ' -f 1)"
kernel="$(uname -r)"
cpus="$(nproc)"
res=""

separate_output=0
opts_short="lkchs"
opts_long="load,kernel,cpus,help,script"
getopt -Q -o "$opts_short" -l "$opts_long" -- "$@" || exit 1
# parse acctual arguments
eval set -- "$( getopt -o "$opts_short" -l "$opts_long" -- "$@" )"

if [ "$#" -eq 1 ]; then
    echo "load=$load kernel=$kernel cpus=$cpus"
elif [ "$#" -eq 2 ] & [ $1 == "-s" ]; then
    echo "load=$load"
    echo "kernel=$kernel"
    echo "cpus=$cpus"
else
    while [ $# -gt 0 ]; do

        case "$1" in
            -l | --load) res="${res}load=$load ";;
            -k | --kernel) res="${res}kernel=$kernel ";;
            -c | --cpus) res="${res}cpus=$cpus ";;
            -s | --script) separate_output=1;;
            -h | --help)
                echo "this is help"
                break;;
        esac
        shift
    done

    if [ $separate_output -eq 1 ]; then
        echo $res | tr ' ' '\n' | cat
    else
        echo "$res"
    fi
fi