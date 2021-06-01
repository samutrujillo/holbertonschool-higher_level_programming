#!/usr/bin/python3
"""  class Student """


class Student():
    """ constructor """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ class dictionary JSON """
        if type(attrs) == list and all(type(items) == str for items in attrs):
            dict = {}
            for i in attrs:
                if i in self.__dict__:
                    dict[i] = self.__dict__[i]
            return dict
        return self.__dict__

    def reload_from_json(self, json):
        """ Replace all attributes"""
        for key, value in json.items():
            self.__dict__[key] = value
