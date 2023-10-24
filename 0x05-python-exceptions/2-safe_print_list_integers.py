#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        ctr = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                ctr += 1
        print()
        return ctr
    except IndexError:
        raise
    except Exception:
        print()
        return ctr
