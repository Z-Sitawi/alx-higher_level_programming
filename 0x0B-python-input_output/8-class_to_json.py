#!/usr/bin/python3
""" function returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
"""


def class_to_json(obj):
    """

    :param obj: is an instance of a Class
    :return: the dictionary description with simple data structure
    """
    return obj.__dict__
