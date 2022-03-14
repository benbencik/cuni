#!/bin/bash

# set -ueo pipefail
# tr '|' '0' | tr ' ' '+' | tr --squeeze-repeats '+' | bc

# cat <&0 | tr '|' '0' | tr ' ' '+' | tr --squeeze-repeats '+' | bc | cat
# tr ' ' '|' < inp_row_sum | cat
# cat - | tr ' ' '+' | echo

tr \| 0|tr -s \  + |bc