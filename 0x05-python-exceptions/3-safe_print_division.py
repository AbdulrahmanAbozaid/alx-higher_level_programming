#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        val = a / b
    except Exception:
        val = None
    finally:
        print("Inside result: ", end="")
        print("{}".format(val))
        return val
