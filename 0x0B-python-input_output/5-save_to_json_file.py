#!/usr/bin/python3
""" function that writes an Object to a text file by JSON """
import json


def save_to_json_file(my_obj, filename):
    """ function """
    with open(filename, 'w') as fichero:
        fichero.write(json.dumps(my_obj))
