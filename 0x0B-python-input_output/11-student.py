#!/usr/bin/python3
'''Test Mod'''


class Student:
    '''Stu Class'''

    def __init__(self, first_name, last_name, age):
        '''Init stud'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Test Func'''

        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, val in self.__dict__.items():
            if key in attrs:
                my_dict[key] = val
        return my_dict

    def reload_from_json(self, json):
        '''Reload Json'''

        for key, val in json.items():
            if key in self.__dict__:
                self.__dict__[key] = val
