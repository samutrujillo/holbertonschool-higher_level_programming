#!/usr/bin/python3
""" Multiply two matrix """


def matrix_mul(m_a, m_b):
    """function"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not all(type(l) is list for l in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(l) is list for l in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(type(i) in [int, float]
               for i in [aux for row in m_a for aux in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all(type(i) in [int, float]
               for i in [aux for row in m_b for aux in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_m = []
    for row in range(len(m_a)):
        new_r = []
        for col in range(len(m_b[0])):
            aux = 0
            for i in range(len(m_a[0])):
                    aux += m_a[row][i] * m_b[i][col]
            new_r.append(aux)
        new_m.append(new_r)

    return new_m
