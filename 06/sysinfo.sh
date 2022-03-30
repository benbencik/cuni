#!/bin/bash
set -ueo pipefail

load="$(cat /proc/loadavg | cut -d ' ' -f 1)"
kernel="$(uname -r)"
cpus="$(nproc)"
res=""
l=0; k=0; c=0; s=0; h=0
args_num="$#"

opts_short="lkchs"
opts_long="load,kernel,cpus,help,script"
getopt -Q -o "$opts_short" -l "$opts_long" -- "$@" || exit 1
eval set -- "$( getopt -o "$opts_short" -l "$opts_long" -- "$@" )"

if [ $args_num -eq 0 ]; then
    l=1; k=1; c=1
else
    while [ $# -gt 0 ]; do
        case "$1" in
            -l | --load) l=1;;
            -k | --kernel) k=1;;
            -c | --cpus) c=1;;
            -s | --script) 
                s=1
                # if there are no other arguments
                if [ $args_num -eq 1 ]; then
                    l=1; k=1; c=1
                fi
                ;;
            -h | --help) h=1;;
        esac
        shift
    done
fi

# append to the res in desired order
if [ "$l" -eq 1 ]; then
    res="${res}load=$load "
fi
if [ "$k" -eq 1 ]; then
    res="${res}kernel=$kernel "
fi
if [ "$c" -eq 1 ]; then
    res="${res}cpus=$cpus "
fi

# remove the last character
res=${res::-1}

# printing
if [ "$h" -eq 1 ]; then
    echo "Usage: sysinfo [options]"
    echo " -c   --cpu     Print number of CPUs."
    echo " -l   --load    Print current load."
    echo " -k   --kernel  Print kernel version."
    echo " -s   --script  Each value on separate line."
    echo ""
    echo "Without arguments behave as with -c -l -k."
    echo ""
    echo "Copyright NSWI177 2022"
elif [ "$s" -eq 1 ]; then
    echo "$res" | tr ' ' '\n'
else
    echo $res
fi
