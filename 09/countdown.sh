#!/bin/bash

set -ueo pipefail

on_exit() {
    echo "Aborted"
    trap - EXIT
    exit 17
}


trap "on_exit" INT


for ((i=$1; i > 0; i--)); do
    echo "$i"
    sleep 1
done
