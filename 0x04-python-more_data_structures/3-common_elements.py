#!/usr/bin/python3
def common_elements(set_1, set_2):
    """  returns a set of common elements in two sets """
    s = []
    i = 0
    for x in set_1:
        for y in set_2:
            if x == y:
                s.append(x)
    return s
