#!/usr/bin/python3
""" 10-main """
import sys


if __name__ == "__main__":
    sys.path.append("..")
    from models.square import Square

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
