#!/usr/bin/env python3
import os

def rec_print(path, indentation):
    curr_dir = os.scandir(path)
    items = []
    dir = {}

    for thing in curr_dir:
        items.append(thing.name)
        if thing.is_dir(): dir[thing.name] = True
        else: dir[thing.name] = False
    
    items.sort()

    if indentation == 0: path=''
    for x in items:
        if (x[0] != '.'):
            if dir[x]:
                print('\t'*indentation + x + '/')
                rec_print(os.path.join(path, x), indentation+1)
            else: 
                print('\t'*indentation + x)


def main():
    cwd = os.getcwd()
    rec_print(cwd, 0)


if __name__ == '__main__':
    main()