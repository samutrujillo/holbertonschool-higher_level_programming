#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sys.path.append("..")
    max_integer = __import__('9-max_integer').max_integer

    my_list = [1, 90, 232, 13, 300, 5, -13, 5]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))