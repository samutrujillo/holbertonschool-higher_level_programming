#!/usr/bin/python3
"""
class  that prevents the user from dynamically creating new
instance attributes, except if the new instance attribute is called first_name.
"""


class LockedClass():
    """constructor"""
    __slots__ = "first_name"
