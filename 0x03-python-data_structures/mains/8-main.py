#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sys.path.append("..")
    multiple_returns = __import__('8-multiple_returns').multiple_returns

    sentence = "At Holberton school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))