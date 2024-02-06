#!/usr/bin/python3
'''Module Test'''


def append_write(filename="", text=""):
    '''Function Tesr'''

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
