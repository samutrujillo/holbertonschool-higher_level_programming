#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    class_to_json = __import__('8-class_to_json').class_to_json

class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)
