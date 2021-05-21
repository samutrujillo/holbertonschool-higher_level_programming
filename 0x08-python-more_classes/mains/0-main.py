#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    Rectangle = __import__('0-rectangle').Rectangle

    my_rectangle = Rectangle()
    print(type(my_rectangle))
    print(my_rectangle.__dict__)