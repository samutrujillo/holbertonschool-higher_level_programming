#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    Square = __import__('10-square').Square

    s = Square(13)

    print(s)
    print(s.area())
