#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """  returns a set of all elements present in only one set """
    elements = set()
    for x in set_1:
        if x not in set_2 and x not in elements:
            elements.add(x)
    for y in set_2:
        if y not in set_1 and y not in elements:
            elements.add(y)

    return elements
