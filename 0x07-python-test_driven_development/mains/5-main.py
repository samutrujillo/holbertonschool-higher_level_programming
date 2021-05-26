#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    max_integer = __import__('6-max_integer').max_integer

    print(max_integer([1, 2, 3, 4]))
    print(max_integer([1, 3, 4, 2]))
