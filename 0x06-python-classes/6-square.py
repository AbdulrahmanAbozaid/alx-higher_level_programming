#!/usr/bin/python3
"""Square Module define squares"""


class Square:
    """Square Class to define squares """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square"""
        self.size = size
        self.position = position

    @property
    def position(self):
        """Getter of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position Setter Method"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        """print the square"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
