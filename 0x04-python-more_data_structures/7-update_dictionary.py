#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """ This function replaces or adds key/value in a dictionary
    * @key argument will be always a string
    * @value argument will be any type
    * If a key exists in the dictionary, the value will be replaced
    * If a key doesn’t exist in the dictionary, it will be created
    """
    if isinstance(a_dictionary, dict):
        if key not in a_dictionary or key in a_dictionary:
            a_dictionary[key] = value
    return a_dictionary
