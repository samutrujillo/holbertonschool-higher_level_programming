#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    append_after = __import__('100-append_after').append_after

    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
