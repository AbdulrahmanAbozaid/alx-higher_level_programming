#!/usr/bin/python3
"""Module draw Square"""


def print_square(size):
    """print a square args"""

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        if i < size - 1:
            print("")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
