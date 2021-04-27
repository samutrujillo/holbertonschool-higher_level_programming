#!/usr/bin/env python3
import sys


if __name__ == '__main__':
    sys.path.append('..')
uppercase = __import__('8-uppercase').uppercase

uppercase("holberton")
uppercase("Holberton School 98 Battery street")
