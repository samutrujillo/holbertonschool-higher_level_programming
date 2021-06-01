#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    write_file = __import__('3-write_file').write_file

    nb_characters = write_file("my_first_file.txt", "Holberton School is so cool!\n")
    print(nb_characters)
