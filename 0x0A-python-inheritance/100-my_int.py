#!/usr/bin/python3
'''MyInt Class'''


class MyInt(int):
    '''MyInt Class'''

    def __new__(cls, *args, **kwargs):
        '''Create New Inst'''

        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        '''Equalty'''

        return int(self) != other

    def __ne__(self, other):
        '''Equalty'''

        return int(self) == other
