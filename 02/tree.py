import os

def rec_print(path, indentation):
    curr_dir = os.scandir(path)
    files, directories = [], []
    for thing in curr_dir:
        if thing.is_dir(): directories.append(thing.name)
        elif (thing.is_file(follow_symlinks=False)): files.append(thing.name)
    
    directories.sort()
    files.sort()

    if indentation == 0: path=''
    for d in directories:
        if d[0] != '.':
            print('\t'*indentation + d + '/')
            rec_print(os.path.join(path, d), indentation+1)
    for f in files:
        if f[0] != '.': print('\t'*indentation + f)


def main():
    cwd = os.getcwd()
    rec_print(cwd, 0)


if __name__ == '__main__':
    main()