#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ replaces an element in a list at a specific position without modifying the original list"""
    list_copy = []
    if isinstance(my_list, list):
        list_copy = my_list.copy()
    if idx < 0:
        return list_copy
    elif idx >= len(my_list):
        return list_copy
    else:
        list_copy[idx] = element
        return list_copy
