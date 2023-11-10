#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ adds all unique integers in a list """
    some = 0
    for x in my_list:
        some = some + x
    return some


my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))