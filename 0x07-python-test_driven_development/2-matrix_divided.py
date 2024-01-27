#!/usr/bin/python3
""" module to divide mats """


def matrix_divided(matrix, div):
    """Matrix division process """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    for r in matrix:
        if not isinstance(r, list) or len(r) == 0:
            raise TypeError("matrix must be a matrix " +
                            "(list of lists) of integers/floats")
        if len(r) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for a in r:
            if not isinstance(a, (int, float)):
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")
    return [[round(a / div, 2) for a in row] for row in matrix]


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/2-matrix_divided.txt')
