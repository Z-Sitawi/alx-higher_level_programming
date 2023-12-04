#!/usr/bin/python3
"""Defines a class-checking function."""


def inherits_from(obj, a_class):
    """
    :param obj: An object
    :param a_class: specified class
    :return: True if the object is an instance of a class that inherited
                (directly or indirectly) from the specified class.
             False otherwise.
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
