#!/usr/bin/python3
def best_score(a_dictionary):
    """ returns a key with the biggest integer value """
    if isinstance(a_dictionary, dict) or len(a_dictionary) != 0:
        # get value of the first key.
        key = list(a_dictionary.keys())[0]
        big = a_dictionary[key]
        # compare it with the rest values.
        for k, v in a_dictionary.items():
            if v > big:
                big = v
                key = k
        return key
    else:
        return None
