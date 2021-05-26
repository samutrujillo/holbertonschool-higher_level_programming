#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    print_square = __import__('4-print_square').print_square

    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(2)
    print("")
    print_square(0.4)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
