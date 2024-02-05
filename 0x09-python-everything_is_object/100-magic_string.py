#!/usr/bin/python3
x = 0


def magic_string():
    return str("BestSchool, " * (x := x + 1))[:-2]
