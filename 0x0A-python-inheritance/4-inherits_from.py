#!/usr/bin/python3
'''Sub class'''


def inherits_from(obj, a_class):
    '''Inherits From Class'''

    return isinstance(obj, a_class) and type(obj) != a_class
