#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    element_at = __import__('1-element_at').element_at

    my_list = [1, 2, 3, 4, 5]
    idx = 3
    print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))