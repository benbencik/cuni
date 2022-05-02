import json
import sys
import json
import tap

args = sys.argv
loader = tap.loader.Loader()
parser = tap.parser.Parser()

for file in args[1:]:
    for line in parser.parse_line(file):
        print(line)