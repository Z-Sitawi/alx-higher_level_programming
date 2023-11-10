#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ prints a dictionary by ordered keys """
    keys = []
    for x, y in a_dictionary.items():
        keys.append("{}: {}".format(x, y))
        keys.sort()
    for i in keys:
        print(i)
