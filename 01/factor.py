#!/usr/bin/env python3
import math

def main():
    with open("input.txt") as f:
        num = int(f.readline())
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

if __name__ == '__main__':
    main()
