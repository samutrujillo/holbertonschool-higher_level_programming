#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """ function """
    with open(filename, encoding="utf-8") as fichero:
        for line in fichero:
            print(line, end="")
