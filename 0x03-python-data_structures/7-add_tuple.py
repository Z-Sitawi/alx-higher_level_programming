#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """ this function that adds 2 tuples and returns a new tuple"""

    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if 0 < len_a < 2 or len_a > 2:
        tuple_a = (tuple_a[0], 0)
    elif 0 < len_b < 2 or len_b > 2:
        tuple_b = (tuple_b[0], 0)
    elif len_a == 0:
        tuple_a = (0, 0)
    elif len_b == 0:
        tuple_b = (0, 0)

    a = tuple_a[0] + tuple_b[0]
    b = tuple_a[1] + tuple_b[1]
    new_tuple = (a, b)
    return new_tuple
