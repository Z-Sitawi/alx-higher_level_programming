#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """ returns a new dictionary with all values multiplied by 2 """
    new_dic = dict()

    for x in a_dictionary:
        new_dic[x] = a_dictionary.get(x) * 2
    return new_dic
