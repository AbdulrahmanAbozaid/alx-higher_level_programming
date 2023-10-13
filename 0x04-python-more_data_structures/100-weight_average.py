#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    up, down = 0, 0
    for i, j in my_list:
        up += (i * j)
        down += j
    return (up / down)
