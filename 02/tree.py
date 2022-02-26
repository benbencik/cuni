#!/usr/bin/env python3
import os

def rec_print(path, indentation):
    curr_dir = os.scandir(path)
    items = []
    dir = {}

    for thing in curr_dir:
        if (thing.name[0] != '.'):
            
            if thing.is_dir(): 
                items.append(thing.name)
                dir[thing.name] = True
            elif (thing.is_file(follow_symlinks=False)):
                items.append(thing.name)
                dir[thing.name] = False
    
    items.sort()

    if indentation == 0: path=''
    for x in items:
        if dir[x]:
            print('    '*indentation + x + '/')
            rec_print(os.path.join(path, x), indentation+1)
        else: 
            print('    '*indentation + x)


def main():
    cwd = os.getcwd()
    rec_print(cwd, 0)


if __name__ == '__main__':
    main()