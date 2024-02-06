#!/usr/bin/python3
'''Module Test'''


def write_file(filename="", text=""):
    '''Write File'''

    len = 0
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
