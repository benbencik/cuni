#!/bin/bash

# aha ja tu musim nastavit ze to nejako berie input
set -o pipefail
cut -d ':' -f 3  $1 | sort --reverse --numeric-sort | head -n 2 | tac | head -n 1