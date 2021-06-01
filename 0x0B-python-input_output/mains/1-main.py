#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    number_of_lines = __import__('1-number_of_lines').number_of_lines

    filename = "my_file_0.txt"
    nb_lines = number_of_lines(filename)
    print("{} has {:d} lines".format(filename, nb_lines))
