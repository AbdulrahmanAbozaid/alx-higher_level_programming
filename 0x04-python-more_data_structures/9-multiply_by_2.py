#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = {}
    for key, val in a_dictionary.items():
        res[key] = val * 2
    return res
