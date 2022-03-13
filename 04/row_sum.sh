#!/bin/bash

set -ue pipefail
# tr '|' '0' < inp_row_sum | tr ' ' '+' | tr --squeeze-repeats '+' | bc
# tr '|' '0' <&0 | tr ' ' '+' | tr --squeeze-repeats '+' | bc
cat <&0 | xargs tr ' ' '|' | cat
# tr ' ' '|' < inp_row_sum | cat