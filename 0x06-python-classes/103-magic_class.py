#!/usr/bin/python3
""" MagicClass """
import math


class MagicClass:
    """ Magic instances """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    """ Computes area """
    def area(self):
        return self.__radius ** 2 * math.pi

    """ Computes circunference """
    def circumference(self):
        return 2 * math.pi * self.__radius
