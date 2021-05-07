#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))