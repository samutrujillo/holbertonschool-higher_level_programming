#!/usr/bin/python3
"""unction that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """function"""
    try:
        name = "My name is"
        if type(first_name) is not str:
            raise TypeError('first_name must be a string')
        if type(last_name) is not str:
            raise TypeError('last_name must be a string')
        print("{} {} {}".format(name, first_name, last_name))
    except:
        raise
