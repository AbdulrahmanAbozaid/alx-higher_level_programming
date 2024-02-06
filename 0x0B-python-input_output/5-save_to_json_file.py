#!/usr/bin/python3
'''user mod'''


import json


def save_to_json_file(my_obj, filename):
    '''Test Func'''

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
