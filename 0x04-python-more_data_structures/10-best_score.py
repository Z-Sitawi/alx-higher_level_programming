#!/usr/bin/python3
def best_score(a_dictionary):
    """ returns a key with the biggest integer value """
    if isinstance(a_dictionary, dict):
        # find the biggest value.
        val = []
        for x in a_dictionary.values():
            val.append(x)
        val = sorted(val)
        biggest = val[len(val) - 1]
        # find the key of biggest value.
        for key in a_dictionary:
            if a_dictionary.get(key) == biggest:
                return key
