#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    ctr = 0
    argc = len(argv) - 1
    for i in range(argc):
        ctr += int(argv[i + 1])
    print(ctr)
