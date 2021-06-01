#!/usr/bin/python3
""" function that returns an object by JSON """
import json


def from_json_string(my_str):
    """ function """
    return json.loads(my_str)
