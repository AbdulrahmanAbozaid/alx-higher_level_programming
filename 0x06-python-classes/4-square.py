#!/usr/bin/python3
"""Square Module define squares"""


class Square:
    """Square Class to define squares """
    def __init__(self, size=0):
        """Initialize Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def area(self):
        """Square Area """
        return self.size ** 2

    @property
    def size(self):
        """Getter of sizze"""
        return self.__size

    @size.setter
    def size(self, value):
        """Size Setter Method"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
