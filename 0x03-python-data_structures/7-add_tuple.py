#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = ()
    res += (0 if len(tuple_a) < 1 else tuple_a[0]) +\
        (0 if len(tuple_b) < 1 else tuple_a[0]),
    res += (0 if len(tuple_a) < 2 else tuple_a[1]) +\
        (0 if len(tuple_b) < 2 else tuple_a[1]),
    return res
