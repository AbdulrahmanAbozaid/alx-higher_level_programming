#!/usr/bin/python3
"""Square Module define squares"""


class Square:
    """Square Class to define squares """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple)\
                or len(position) != 2 or not isinstance(position[0], int)\
                or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.size = size
        self.position = position

    @property
    def position(self):
        """Getter of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Position Setter Method"""
        if not isinstance(value, tuple) or len(value) != 2\
                or not isinstance(value[0], int)\
                or not isinstance(value[1], int):
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
            print()
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[0]):
                    print()

            for i in range(self.__size):
                if self.__position[0] > 0:
                    for i in range(self.__position[0]):
                        print(" ", end="")
                print('#' * self.__size)
