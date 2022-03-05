#!/bin/python3

import sys
def usage(output):
    print("Usage: {} NUMBER".format(sys.argv[0]), file=output)
    print("...")
def main():
    if len(sys.argv) != 2:
        usage(sys.stderr)
        sys.exit(2)
    if sys.argv[1] == "--help":
        usage(sys.stdout)
        sys.exit(0)
    try:
        number = int(sys.argv[1])
        if number % 2 == 0:
            sys.exit(0)
        else:
            sys.exit(1)
    except ValueError:
        usage(sys.stderr)
        sys.exit(2)
if __name__ == '__main__':
    main()