#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i, num in enumerate(my_list):
        if num == search:
            new_list[i] = replace
    return new_list
