#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if not (key in a_dictionary) or key == "":
        return a_dictionary
    del a_dictionary[key]
    return a_dictionary
