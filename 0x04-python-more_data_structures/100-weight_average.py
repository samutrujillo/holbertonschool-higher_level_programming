#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    aux = 0
    aux2 = 0
    for i, j in my_list:
        aux += i * j
        aux2 += j
    return (aux / aux2)
