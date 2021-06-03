#!/usr/bin/python3
""" class BaseGeometry """


class BaseGeometry:
    """ constructor """
    def area(self):
        """ function """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ function """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
