#!/usr/bin/python3
""" function that writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """ function """
    with open(filename, 'w', encoding='utf8') as fichero:
        return fichero.write(text)
