#!/usr/bin/python3
'''Binary Pyth'''


import json


def load_from_json_file(filename):
    '''Bin Pyth'''

    with open(filename, encoding='utf-8') as f:
        return json.load(f)
