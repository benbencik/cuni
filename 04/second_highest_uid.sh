#!/bin/bash

# cut -d ':' -f 3  /etc/passwd | sort | head
cut -d ':' -f 3  /etc/passwd | sort --reverse --numeric-sort | head -n 2 | tac | head -n 1