#!/bin/bash

set -ueo pipefail

on_exit() {
    echo "Aborted"
    trap - EXIT
    exit 17
}


trap "on_exit" INT


for num in {10..1}; do
    echo $num
    sleep 1
done
