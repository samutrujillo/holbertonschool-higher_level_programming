#!/usr/bin/python3
"""
 class Square that defines a square
"""


class Square():
    """constructor"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """method to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """method to set it"""
        try:
            if not isinstance(value, int):
                raise TypeError()
            if value < 0:
                raise ValueError()
            self.__size = value
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    def area(self):
        """ square area"""
        return self.__size ** 2

    def my_print(self):
        """print square with the #"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
