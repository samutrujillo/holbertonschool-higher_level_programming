#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    LockedClass = __import__('101-locked_class').LockedClass

    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
