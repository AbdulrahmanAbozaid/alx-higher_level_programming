#!/usr/bin/python3
def common_elements(set_1, set_2):
    res = []
    for i in set_1:
        if list(set_2).count(i):
            res.append(i)
    return res
