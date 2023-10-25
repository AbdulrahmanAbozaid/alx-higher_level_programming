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
        self.__size = size
