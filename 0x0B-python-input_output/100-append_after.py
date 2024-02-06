#!/usr/bin/python3
'''Test Py'''


def append_after(filename="", search_string="", new_string=""):
    '''Append After'''

    with open(filename, 'r', encoding='utf-8') as f:
        ln = []
        while True:
            line = f.readline()
            if line == '':
                break
            ln.append(line)
            if search_string in line:
                ln.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(ln)
