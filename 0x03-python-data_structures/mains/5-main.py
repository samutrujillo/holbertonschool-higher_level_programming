#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sys.path.append("..")
    no_c = __import__('5-no_c').no_c

    print(no_c("Holberton School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))