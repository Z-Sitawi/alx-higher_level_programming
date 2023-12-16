#!/usr/bin/python3
""" Prints a square with the # character."""


def print_square(size):
    """
    :param size: the size length of the square

    :raise TypeError: if size is not an integer.
    :raise ValueError: if size is less than 0.
    :raise TypeError: if size is a float and is less than 0
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    for h in range(size):
        for w in range(size):
            print("#", end="")
        print("")
