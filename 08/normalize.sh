#!/bin/bash
set -ueo pipefail

# get rid of prev folders | special case /a/.. | get ridd of current
echo $1 | sed 's#/\.\/#/#g' | sed ':x; s#/[a-z|_|.]*/\.\./#/#; tx' | sed 's#^[a-z|_|.]*/\.\./##g'
# | sed ':x; s/abb/ba/; tx' 