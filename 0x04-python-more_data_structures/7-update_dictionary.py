#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    tuple1 = {key: value}
    a_dictionary.update(tuple1)
    return a_dictionary
