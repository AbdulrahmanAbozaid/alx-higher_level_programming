#!/usr/bin/python3
'''Square Class Def'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square Class definition'''

    def __init__(self, size):
        '''Init Square'''

        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Area Sled'''

        return self.__size ** 2
