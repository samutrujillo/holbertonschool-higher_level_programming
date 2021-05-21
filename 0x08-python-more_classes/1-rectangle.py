#!/usr/bin/python3
""" class rectangle """


class Rectangle:
    """ constructor """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def width(self):
        self.__width
        
    @width.setter
    def width(self, value):
        try:
            if type(value) is not int:
                raise TypeError('width must be an integer')
            if value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value
        except:
            raise
        
    @property
    def height(self):
        self.__height
        
    @height.setter
    def height(self, value):
        try:
            if type(value) is not int:
                raise TypeError('height must be an integer')
            if value < 0:
                raise ValueError('height must be >= 0')
            self.__height = value
        except:
            raise
