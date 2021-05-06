#!/usr/bin/python3
def multiple_returns(sentence):
    a = None
    tam = len(sentence)
    if tam > 0:
        a = sentence[0]
    return tam, a
