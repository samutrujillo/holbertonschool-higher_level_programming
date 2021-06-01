#!/usr/bin/python3
""" Defines pascal triangle """


def pascal_triangle(n):
    """ Prints pascal triangle """
    if n <= 0:
        return []
    tri = []
    row = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(i):
                row.append(sum(tri[-1][j:j+2]))
        tri.append(row)
    return tri
