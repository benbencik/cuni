#!/usr/bin/env python3

import sys

def main():
    for i, arg in enumerate(sys.argv):
        print("argv[{}]: '{}'".format(i, arg))
    for line in sys.stdin:
        print("stdin: '{}'".format(line.rstrip('\n')))
    sys.exit(0)

if __name__ == '__main__':
    main()
