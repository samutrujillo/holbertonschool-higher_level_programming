#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """constructor"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """method to retrieve ir"""
        return self.__width

    @width.setter
    def width(self, value):
        """method to set it"""
        try:
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        except:
            raise

    @property
    def height(self):
        """ method to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """method to set it"""
        try:
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        except:
            raise

    def area(self):
        """ rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """rectangle perimeter:"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        empty_string = ""
        if self.__height == 0 or self.width == 0:
            return empty_string
        for i in range(self.__height):
            empty_string += ("#" * self.__width)
            if i is not self.__height - 1:
                empty_string += "\n"
        return empty_string

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
