#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    matrix_mul = __import__('100-matrix_mul').matrix_mul

    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
