#!/usr/bin/python3
""" function that adds a new attribute to an object if it’s possible """


def add_attribute(obj, name, value):
    """ function """
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
