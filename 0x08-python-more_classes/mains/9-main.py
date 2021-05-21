#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    Rectangle = __import__('9-rectangle').Rectangle

    my_square = Rectangle.square(5)
    print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
    print(my_square)