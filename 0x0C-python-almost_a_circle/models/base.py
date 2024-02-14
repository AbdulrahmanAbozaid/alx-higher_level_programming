#!/usr/bin/python3
"""Model of Almost A Circle"""
from json import dumps, loads
import csv
from turtle import pen, pendown


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string"""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a new dictionary"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            obj = Rectangle(2, 2)
        else:
            obj = Square(2)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """load a dictionary from a file"""
        try:
            with open("{}.json".format(cls.__name__),
                      'r', encoding='utf-8') as f:
                list_objs = cls.from_json_string(f.read())
                return [cls.create(**obj) for obj in list_objs]
        except FileNotFoundError as e:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save a dictionary"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            fields = [
                [obj.id, obj.width,
                 obj.height, obj.x, obj.y] for obj in list_objs
            ]
        elif cls is Square:
            fields = [
                [obj.id, obj.size,
                 obj.x, obj.y] for obj in list_objs
            ]
        with open('{}.csv'.format(cls.__name__), 'w',
                  newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerows(fields)

    @classmethod
    def load_from_file_csv(cls):
        """Load from a CSV file"""
        from models.rectangle import Rectangle
        from models.square import Square
        res = []
        with open('{}.csv'.format(cls.__name__), 'r',
                  newline='', encoding='utf-8') as cf:
            reader = list(csv.reader(cf, delimiter=','))
        if cls is Rectangle:
            return [
                cls.create(**{
                    "id": int(row[0]),
                    "width": int(row[1]),
                    "height": int(row[2]),
                    "x": int(row[3]),
                    "y": int(row[4]),
                }) for row in reader
            ]
        elif cls is Square:
            return [
                cls.create(**{
                    "id": int(row[0]),
                    "size": int(row[1]),
                    "x": int(row[2]),
                    "y": int(row[3]),
                }) for row in reader
            ]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw the objects"""
        import turtle
        from random import randrange
        import time
        objs = list_rectangles + list_squares
        turtle.Screen().colormode(255)
        for obj in objs:
            t = turtle.Turtle()
            t.color((randrange(0, 255), randrange(0, 255), randrange(0, 255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos(obj.x + t.pos()[0], obj.y - t.pos()[1])
            t.pensize(7)
            t.fd(obj.width)
            t.left(90)
            t.fd(obj.height)
            t.left(90)
            t.fd(obj.width)
            t.left(90)
            t.fd(obj.height)
            t.end_fill()
            time.sleep(1)
        time.sleep(5)
