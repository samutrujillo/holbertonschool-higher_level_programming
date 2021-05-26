#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    matrix_divided = __import__('2-matrix_divided').matrix_divided

    matrix = [
        [2, 4],
        [4, 3]
    ]
    """matrix_2 = [
        {"a": 2,"b": 3,"c": 4},
        {"d": 5,"s": 6,"h": 7}
    ]"""
    print(matrix_divided(matrix, None))
    print(matrix)
    #print(matrix_divided(matrix_2, 3))
    #print(matrix_2)
