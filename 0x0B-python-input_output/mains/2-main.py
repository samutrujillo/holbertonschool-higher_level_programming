#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    read_lines = __import__('2-read_lines').read_lines

    print("1 line:")
    read_lines("my_file_0.txt", 1)
    print("--")
    print("3 lines:")
    read_lines("my_file_0.txt", 3)
    print("--")
    print("Full content:")
    read_lines("my_file_0.txt")
