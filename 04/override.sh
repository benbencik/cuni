#!/bin/bash

# print contains of headers
# if .NO_HEADER is in directory nothing is printed
# if there is none echo "Error: HEADER not found"

set -o pipefail
test -f .NO_HEADER || cat HEADER 2> /dev/null && echo "Error: HEADER not found." >&2
# test -f .NO_HEADER || cat HEADER 2> /dev/null && echo