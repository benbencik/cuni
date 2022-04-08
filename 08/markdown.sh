#!/bin/bash
set -ueo pipefail

# emphasis | strong | links | 
sed 's#_\([a-z A-Z0-9]*\)_#<em>\1<\\em>#g' | 
sed 's#\*\([a-z A-Z0-9]*\)\*#<strong>\1<\\strong>#g' | 
sed 's#[(http://|https://)]\(*\)|\(*\)]#<a href="http://\1">\2</a>>#g' |
sed 's#\[\(.*\)|\(.*\)\]#<a href="\1">\2</a>>#g' | sed 's#https://#http://#g'
# (http://|https://)
# <a href="http://"></a>>