# #!/bin/bash
# set -ueo pipefail

# repeat_string() {
#     local i
#     for i in $( seq $1 ); do
#         echo -n "$2"
#     done
# }

# temp_dir="$( mktemp -d )"
# longest_bar=""

# # COLUMNS=20
# # if there is no value set it to default
# if [ -z $COLUMNS ]; then
#     COLUMNS=80
# fi 


# while read len name || [ -n "$len" ]; do
#     # if [ "$len" == "#" ]; then
#     #     screen_width="$(echo $name | cut -d "=" -f 2)"
#     # else

#     # load values into file
#     echo "$len $name" >> $temp_dir/data
#     # set the maximum
#     [ -z "$longest_bar" ] && longest_bar="$len"
#     if [ "$len" -gt "$longest_bar" ]; then
#         longest_bar="$len";
#     fi
# done < $1


# longest_label="$(wc -L "$temp_dir/data" | cut -d " " -f 1)"
# longest_label="$(( longest_label + 5))"
# # actual space dedicated for the bar
# space_for_bar="$(( "$COLUMNS" - "$longest_label" ))"

# # scaling of the bar
# if [ "$longest_bar" -gt "$space_for_bar" ]; then
#     # do not compute for better precision later on
#     scale="$space_for_bar / $longest_bar"
# else
#     scale="$space_for_bar / $longest_bar"
# fi


# while read len name || [ -n "$len" ]; do
#     # $scale must not be quoted (it may contain an expression)
#     size="$(( $len * $scale ))"

#     label_len="$( echo $len $name | wc -m)"
#     label_len="$(( $label_len+4 ))"
#     additional_space="$(( $longest_label - $label_len ))"
#     printf "%s (%d) %s| %s\n" "$name" "$len" "$( repeat_string "$additional_space" " " )" "$( repeat_string "$size" "#" )"
# done < "$temp_dir/data"