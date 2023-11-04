#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    start = len(my_list)
    for x in my_list:
        start = start - 1
        tmp = x
        x = my_list[start]
        my_list[start] = tmp
        print("{:d}".format(x))
