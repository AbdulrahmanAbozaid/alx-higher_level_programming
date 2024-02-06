#!/usr/bin/python3
"""Files Handle"""


def read_file(filename=""):
    '''Read File'''

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
