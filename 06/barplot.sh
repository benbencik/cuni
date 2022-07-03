# #!/bin/bash

# set -eu

# plot_line() {
#     for i in $(seq "$inp"); do
#     echo "$i" > /dev/null
#         echo -n '#'
#     done
# }

# max=0;

# for inp in "$@"; do
#     if [ "$inp" -ge "$max" ]; then
#         max=$inp
#     fi
# done

# if [ "$max" -ge 60 ]; then
#     for inp in "$@"; do
#         plot_line "$inp"
#         echo
#     done
# else
#     ratio="$(( max / 60 ))"
#     for inp in "$@"; do
#         plot_line "$(( inp * ratio ))"
#         echo
#     done
# fi