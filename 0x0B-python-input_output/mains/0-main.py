#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    read_file = __import__('0-read_file').read_file

    read_file("my_file_0.txt")
