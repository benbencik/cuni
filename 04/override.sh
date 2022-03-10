#!/bin/bash

# print contains of headers
# if .NO_HEADER is in directory nothing is printed
# if there is none echo "Error: HEADER not found"

test -f .NO_HEADER > /dev/null || cat HEADER 2> /dev/null || echo "Error: HEADER not found"