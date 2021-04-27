#!/usr/bin/env python3
import sys


if __name__ == '__main__':
    sys.path.append('..')
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")
