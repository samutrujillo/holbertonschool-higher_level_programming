#!/usr/bin/python3
""" function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ function """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix " +
                        "(list of lists) of integers/floats")
    sub_l_len = 0
    for sub_l in matrix:
        for i in sub_l:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")

        if sub_l_len == 0:
            sub_l_len = len(sub_l)
        elif sub_l_len != len(sub_l):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in sub_l] for sub_l in matrix]
