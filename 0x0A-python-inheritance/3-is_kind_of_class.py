#!/usr/bin/python3
"""Defines a class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    :param obj: An object
    :param a_class: specified class
    :return: True if the object is an instance of the specified class,
            or if the object is an instance of a class that inherited from the specified class.
             False otherwise.
    """
    if type(obj) is a_class or issubclass(type(obj), a_class):
        return True
    else:
        return False
