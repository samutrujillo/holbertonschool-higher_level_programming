#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    a = len(argv)
    if a < 2:
        print('0 arguments.')
    elif a == 2:
        print('1 argument:')
    else:
        print('{:d} arguments:'.format(a - 1))
    for i in range(1, a):
        print('{:d}: {}'.format(i, argv[i]))
