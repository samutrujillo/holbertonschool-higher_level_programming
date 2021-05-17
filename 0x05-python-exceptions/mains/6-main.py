#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)