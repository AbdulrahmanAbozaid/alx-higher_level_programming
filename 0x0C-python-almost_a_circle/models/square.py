#!/usr/bin/python3
"""Model of Almost A Circle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """init square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """set size of square"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """update square"""
        if id:
            self.id = id
        if size:
            self.size = size
        if x:
            self.x = x
        if y:
            self.y = y

    def update(self, *args, **kwargs):
        """update square"""
        if len(args):
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """to_dictionary"""
        return {"id": self.id, "x": self.x,
                "size": self.width, "y": self.y}
