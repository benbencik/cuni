import sys
import json
from tap.parser import Parser
import os

files = sys.argv
parser = Parser()
out = {"summary": []}

for f in files[1:]:
    print(f)
    res = {"filename": f, "total": 0, "passed": 0, "skipped": 0, "failed": 0}
    if (os.path.exists(f)):
        inp = parser.parse_file(f)
        for line in inp:
            if (line.category == "test"):
                res["total"] += 1
                if line.ok: res["passed"] += 1
                elif line.skip: res["skipped"] += 1 
                else: res["failed"] += 1
    out["summary"].append(res)
print(json.dumps(out, indent=True))