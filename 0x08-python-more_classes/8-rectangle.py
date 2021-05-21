#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """constructor"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        empty_string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    empty_string += str(self.print_symbol)
                except Exception:
                    empty_string += type(self).print_symbol
            if i is not self.__height - 1:
                empty_string += "\n"
        return empty_string

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

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
