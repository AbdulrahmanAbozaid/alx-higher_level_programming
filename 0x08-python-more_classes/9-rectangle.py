#!/usr/bin/python3
"""Rect Module here"""


class Rectangle:
    """Rectangle based class Implementation"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing an Recangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve width"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for width"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get* Area"""

        return self.__width * self.__height

    def perimeter(self):
        """Get Perimeter of rect."""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String Represent for users"""

        if self.__width == 0 or self.__height == 0:
            return ""
        res = ""
        for i in range(self.__height):
            res += str(self.print_symbol) * self.__width
            res += "\n" if i != self.__height - 1 else ""
        return res

    def __repr__(self):
        """Representation of the objes"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor Behavior func"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Bigger od Equal define"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Square Return Rect."""

        return cls(size, size)
