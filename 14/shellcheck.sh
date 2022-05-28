#!/bin/bash

# cd ..
exit_code=0

assert_is_shellchecked() {
    local severity="${1:-info}"
    # local script="${script:-}"
    local script=$2

    # if [[ -z "${script}" ]]; then
    #     script="${NSWI177_MAIN_SCRIPT:?}"
    # fi

    shellcheck "${script}"
    if [ $? == 1 ]; then
        exit_code=1
    fi
    # if [ "$status" -ne 0 ]; then
    #     exit_code = 1;
    #     echo "$output" \
    #         | batslib_decorate "Shellcheck found following issues (severity $severity)" \
    #         | fail
    # fi
}

# list through directories
for dir in */; do
    for thing in $dir*.sh; do
        if [ -f "$thing" ]; then
            # echo $thing
            assert_is_shellchecked "yeeet" $thing
        fi
    done
done

exit $exit_code;