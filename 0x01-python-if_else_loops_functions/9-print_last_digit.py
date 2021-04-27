#!/usr/bin/python3
def print_last_digit(number):
    a = number % 10
    b = (number % -10) * -1
    if number >= 0:
        print("{}".format(a), end="")
        return(a)
    else:
        print("{}".format(b), end="")
        return(b)
