#!/usr/bin/python3
'''Class Module'''


def add_attribute(obj, key, val):
    '''Functiom Doc'''

    if not hasattr(obj, '__dict__'):
        raise TypeError('can\'t add new attribute')
    setattr(obj, key, val)
