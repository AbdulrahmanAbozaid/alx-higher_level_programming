#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        ctr = 0
        for i in range(x):
            print(my_list[i], end="")
            ctr += 1
        print('\n', end="")
        return ctr
    except Exception:
        print("\n", end="")
        return ctr
