#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ adds all unique integers in a list """
    unique_int = set()
    for x in my_list:
        if x not in unique_int:
            unique_int.add(x)
    return sum(unique_int)
