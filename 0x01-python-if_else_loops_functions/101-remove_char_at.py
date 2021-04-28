#!/usr/bin/python3
def remove_char_at(str, n):
    a = ""
    for i in range(0, len(str)):
        if i != n:
            a += str[i]
    return a
