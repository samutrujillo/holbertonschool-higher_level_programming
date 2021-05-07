#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix[:]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new[i] = list(map(lambda x: x ** 2, matrix[i]))
    return new
