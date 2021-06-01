#!/usr/bin/python3
""" script that adds all arguments to a Python list
and then save them to a file """
from sys import argv
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    try:
        i = load_from_json("add_item.json")
    except:
        pass
        i = []
    for add_list in argv[1:]:
        i.append(add_list)
    save_to_json(i, "add_item.json")
