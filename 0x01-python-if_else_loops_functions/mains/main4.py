#!/usr/bin/env python3
import sys


if __name__ == '__main__':
    sys.path.append('..')
add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))
