#!/usr/bin/python3
'''Test Mod'''


class Student:
    '''Stu Class'''

    def __init__(self, first_name, last_name, age):
        '''Init stud'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Jsoniy Func'''

        return self.__dict__
