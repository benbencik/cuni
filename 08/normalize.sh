#!/bin/bash
set -ueo pipefail

# sed 's#\./#g' 
echo $1 | sed ':x; s#/[a-z|_|.]*/\.\.##; tx' | sed 's#\.\/##g'
# | sed ':x; s/abb/ba/; tx' 