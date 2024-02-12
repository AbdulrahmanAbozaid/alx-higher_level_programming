#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """prop getter"""
        return self.__width

    @property
    def height(self):
        """prop getter"""
        return self.__height

    @property
    def x(self):
        """prop getter"""
        return self.__x

    @property
    def y(self):
        """prop getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """prob getter for width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """prob getter for height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """prob getter for x"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """prob getter for y"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """calc the area"""
        return self.__width * self.__height

    def display(self):
        """display the rect."""
        row = self.__x * ' ' + '#' * self.__width
        rect = [row for r in range(self.__height)]
        print(self.__y * '\n' + '\n'.join(rect))

    def __str__(self):
        """returns the string representation"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"\
            f" - {self.__width}/{self.__height}"

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """updating the rectangle"""
        if id:
            self.id = id
        if width:
            self.width = width
        if height:
            self.height = height
        if x:
            self.x = x
        if y:
            self.y = y

    def update(self, *args):
        """updating the rectangle"""
        self.__update(*args)
