#!/usr/bin/python3
"""Model of Almost A Circle"""


class Base:
    '''Class Base For All'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''init object'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
