#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ deletes a key in a dictionary
        key argument will be always a string
        If a key doesn’t exist, the dictionary won’t change
    """
    if isinstance(a_dictionary, dict):
        if key in a_dictionary:
            del a_dictionary[key]
            return a_dictionary
        return a_dictionary
