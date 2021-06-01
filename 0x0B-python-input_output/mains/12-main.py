#!/usr/bin/python3
import sys
"""
12-main
"""


if __name__ == "__main__":
    sys.path.append("..")
    pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))