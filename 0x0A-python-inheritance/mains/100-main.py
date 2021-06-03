#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    MyInt = __import__('100-my_int').MyInt

    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
