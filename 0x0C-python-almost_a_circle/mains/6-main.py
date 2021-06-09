#!/usr/bin/python3
""" 6-main """
import sys


if __name__ == "__main__":
    sys.path.append("..")
    from models.rectangle import Rectangle

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()
