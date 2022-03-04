#!/usr/bin/env python3
import os
import sys
from traceback import print_tb

def rec_print(path, indentation, only_dirs):
    curr_dir = os.scandir(path)
    items = []
    dir = {}

    for thing in curr_dir:
        if (thing.name[0] != '.'): # do not show hidden files 
            if thing.is_dir(follow_symlinks=False):  # do not show simlinks
                items.append(thing.name)
                dir[thing.name] = True
            elif thing.is_file(follow_symlinks=False):  # do not show simlinks
                items.append(thing.name)
                dir[thing.name] = False
    items.sort()

    if indentation == 0: path=''
    for x in items:
        if dir[x]:
            print('    '*indentation + x + '/')
            rec_print(os.path.join(path, x), indentation+1, only_dirs)
        elif not only_dirs: 
            print('    '*indentation + x)


def main():
    only_dirs = False
    cwd = ''
    for arg in sys.argv:
        if arg == "-d": only_dirs = True
        elif arg[-3:] != ".py": cwd = arg
    if not cwd: cwd = os.getcwd()
    print(cwd)
    rec_print(cwd, 0, only_dirs)


if __name__ == '__main__':
    main()