#!/usr/bin/python3
""" function that creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """ function """
    with open(filename, encoding='utf-8') as fichero:
        return json.loads(fichero.read())
