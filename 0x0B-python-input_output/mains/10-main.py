#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    class_to_json = __import__('10-class_to_json').class_to_json

    m = MyClass("John")
    m.number = 89
    print(type(m))
    print(m)

    mj = class_to_json(m)
    print(type(mj))
    print(mj)
