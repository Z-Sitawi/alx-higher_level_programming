#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ replaces all occurrences of an element by another in a new list."""
    new_list = []
    for x in my_list:
        if x == search:
            new_list.append(replace)
        new_list.append(x)
    return new_list
