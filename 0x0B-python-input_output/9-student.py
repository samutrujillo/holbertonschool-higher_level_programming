#!/usr/bin/python3
""" class Student """


class Student():
    """ constructor """
    def __init__(self, first_name, last_name, age):
        """ Initialize public variables """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ class dictionary JSON """
        return self.__dict__
