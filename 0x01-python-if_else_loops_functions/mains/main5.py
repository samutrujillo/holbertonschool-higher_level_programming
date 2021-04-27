#!/usr/bin/env python3
import sys


if __name__ == '__main__':
    sys.path.append('..')
uppercase = __import__('8-uppercase').uppercase
pow = __import__('11-pow').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
