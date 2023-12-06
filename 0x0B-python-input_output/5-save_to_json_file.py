#!/usr/bin/python3
""" A function that writes an Object to a text file
    using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """

    :param my_obj: the object to convert
    :param filename: the text file to write in
    :return: nothing
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
