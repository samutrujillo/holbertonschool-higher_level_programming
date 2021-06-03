#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    BaseGeometry = __import__('5-base_geometry').BaseGeometry

    bg = BaseGeometry()

    print(bg)
    print(dir(bg))
    print(dir(BaseGeometry))
