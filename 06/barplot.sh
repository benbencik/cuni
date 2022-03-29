#!/bin/bash
set -eu

plot_line() {
    for i in $(seq "$inp"); do
        echo -n '#'
    done
}

$max = 0;co

for inp in "$@"; do
    if $inp > $max; then
        $max = $inp
    fi
done

if $max < 60; then
    for inp in "$@"; do
        plot_line $inp
        echo
    done
else
    $ratio = $max / 60
    for inp in "$@"; do
        plot_line $($inp * $ratio)
        echo
    done
fi