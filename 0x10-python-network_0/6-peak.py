#!/usr/bin/python3
"""
 function
"""


def find_peak(list_of_integers):
    """ return a peak in a list """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
