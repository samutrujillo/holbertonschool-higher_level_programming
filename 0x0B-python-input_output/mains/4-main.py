#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    append_write = __import__('4-append_write').append_write

    nb_characters_added = append_write("file_append.txt", "Holberton School is so cool!\n")
    print(nb_characters_added)
