#!/bin/bash

tDir="${HOME}/.cache/mff_nswi177/tests/repo"

(
cd $tDir
git pull >/dev/null
)

args=""
for f in $@; do
    if [[ -d $f ]]; then
        e=`realpath --relative-to=. $f`/
        [[ -d $tDir/tasks/$e ]]   && args="$args tasks/$e"
        [[ -d $tDir/quizzes/$e ]] && args="$args quizzes/$e"
    else
        e=${f%.*}.bats
        [[ -f $tDir/tasks/$e ]]   && args="$args tasks/$e"
        [[ -f $tDir/quizzes/$e ]] && args="$args quizzes/$e"
    fi
done
args=`echo $args`

#echo bin/run_tests.sh $args
bin/run_tests.sh $argssq