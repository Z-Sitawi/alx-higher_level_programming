#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ return multiples of 2 in a list as a list of tuples."""
    results = []

    for x in my_list:
        if x % 2 == 0:
            results.append(True)
        else:
            results.append(False)
    return results
