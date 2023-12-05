#!/usr/bin/python3
""" a function that returns the JSON representation of an object (string) """
import json


def to_json_string(my_obj):
    """

    :param my_obj: an object
    :return: the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
