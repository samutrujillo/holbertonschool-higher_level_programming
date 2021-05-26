#!/usr/bin/python3
""" function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ function """
    try:
        if not isinstance(div, (float, int)) or isinstance(div, bool):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        if not all(len(lts) == len(matrix[0]) for lts in matrix):
            raise TypeError("Each row of the matrix must have the same size")

        if not isinstance(matrix, list) or \
                len(matrix) == 0 or len(matrix[0]) == 0:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        for a in matrix:
            if not isinstance(a, list) or not len(a) > 0 or not \
                 all(isinstance(column, (int, float)) for column in a):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
        matrix_2 = []
        for i in matrix:
            matrix_2.append(list(map(lambda new_num:
                            round(new_num / div, 2), i)))
        return matrix_2
    except:
        raise
