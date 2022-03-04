#!/usr/bin/env python3
import math
import sys

def factor(inp):
    try: num = int(inp)
    except: 
        print('-')
        return

    if num <= 0: print('-')
    else:
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                print(i)
        print(num)

def main():
    count = 0
    for arg in sys.argv:
        if count != 0: factor(arg)
        count += 1
        

if __name__ == '__main__':
    main()
