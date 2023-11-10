#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ prints a dictionary by ordered keys """
    key, val = [], []
    for x in a_dictionary.keys():
        key.append(x)
    for y in a_dictionary.values():
        val.append(y)
    i = 0
    for z in range(len(key) - 1):
        print("{}: {}".format(key[z], val[z]))


a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3]}
print_sorted_dictionary(a_dictionary)