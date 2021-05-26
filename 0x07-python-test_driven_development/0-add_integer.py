#!usr/bin/python3
"""unction that adds 2 integers"""


def add_integer(a, b=98):
    """method that return a + b"""
    try:
        if isinstance(a, (float, int)) is False:
            raise TypeError("a must be an integer")
        if isinstance(b, (float, int))is False:
            raise TypeError("b must be an integer")
        return(int(a) + int(b))
    except:
        raise
