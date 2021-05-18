#!/usr/bin/python3
"""
class Square that defines a square
"""


class Square:
    """ square size """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """ square area """
    def area(self):
        res = self.__size * self.__size
        return res
