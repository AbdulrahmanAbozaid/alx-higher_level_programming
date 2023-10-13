#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delet = []
    for a, b in a_dictionary.items():
        if b == value:
            delet.append(a)
    for i in range(len(delet)):
        del a_dictionary[delet[i]]
    return a_dictionary
