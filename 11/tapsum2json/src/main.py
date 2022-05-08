#!/usr/bin/env python3

import sys
import json
from tap.parser import Parser
import os

def main():
    files = sys.argv
    parser = Parser()
    out = {"summary": []}

    for f in files[1:]:
        res = {"filename": f, "total": 0, "passed": 0, "skipped": 0, "failed": 0}
        if (os.path.exists(f)):
            inp = parser.parse_file(f)
            expected_tests = 0

            for line in inp:
                if (line.category == "test"):
                    res["total"] += 1
                    if line.skip: res["skipped"] += 1 
                    elif line.ok: res["passed"] += 1
                    else: res["failed"] += 1
                elif (line.category == "plan"):
                    expected_tests = line.expected_tests
                elif (line.category == "bail"):
                    res["total"] = expected_tests
                    res["skipped"] = expected_tests - res["pass"] - res["failed"] 
        out["summary"].append(res)
    print(json.dumps(out, indent=True))

if __name__ == "__main__":
    main()
