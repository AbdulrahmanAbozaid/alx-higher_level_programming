#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    ctr = 0
    for c in str:
        if ctr != n:
            s += c;
        ctr += 1
    return s
