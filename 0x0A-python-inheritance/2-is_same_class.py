#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    :param obj: An object
    :param a_class: specified class
    :return: True if the object is exactly an instance of the specified class;
     otherwise False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
