#!/usr/bin/env python3
import math

def main():
    with open("input.txt") as f:
        num = int(f.readline())
        if num <= 0: print('-')
        else:
            for i in range(1, int(math.sqrt(num))):
                if num % i == 0: print(i)

if __name__ == '__main__':
    main()
