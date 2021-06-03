#!/usr/bin/python3
""" Class MyInit that inherits from Int """


class MyInt(int):
    """ Class """
    def __init__(self, value):
        self.value = value
    """ Change equal to different """
    def __eq__(self, other):
        return self.value != other
    """ Change different to equal """
    def __ne__(self, other):
        return self.value == other
