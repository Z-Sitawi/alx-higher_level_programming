#!/usr/bin/python3
def max_integer(my_list=[]):
    """ a function that finds the biggest integer of a list """
    biggest = my_list[0]
    if my_list is None:
        return None
    for x in my_list:
        if x >= biggest:
            biggest = x
    return biggest

