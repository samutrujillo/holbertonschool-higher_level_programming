#!/usr/bin/python3
""" function that appends a string at the end of a text file (UTF8) """


def append_write(filename="", text=""):
    """ function """
    with open(filename, 'a', encoding='utf8') as fichero:
        return fichero.write(text)
