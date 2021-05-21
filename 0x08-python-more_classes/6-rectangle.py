#!/usr/bin/python3
""" class Rectangle """


class Rectangle:
    """ cosntructor """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        string = ""
        if self.__height == 0 or self.width == 0:
            return string
        for i in range(self.__height):
            string += ("#" * self.__width)
            if i is not self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return(self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 and self.__height == 0:
            return 0
        return(2 * self.__width) + (2 * self.__height)
