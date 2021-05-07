#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    weight_average = __import__('100-weight_average').weight_average

    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    # = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))