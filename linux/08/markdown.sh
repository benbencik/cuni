#!/bin/bash
set -ueo pipefail

sed 's#&#\&amp;#g' | sed 's#<#\&lt;#g' | sed 's#>#\&gt;#g' | sed 's#"#\&quot;#g;' | # entities
sed 's#_\([a-z A-Z0-9]*\)_#<em>\1</em>#g' | # emphasis
sed 's#\*\([a-z A-Z0-9]*\)\*#<strong>\1</strong>#g' | # strong
sed -E 's#\[([^|]*)\|([^]]*)\]#<a href="\1">\2</a>#g' #link
# sed 's#\[\([^|]*\)|\([^\]]*\)\]#brekeke\2#g' # link
