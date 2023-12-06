#!/usr/bin/python3
""" a function that creates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """

    :param filename: the name if the JSON file
    :return: an object
    """
    with open(filename, encoding="utf-8") as file:
        string = file.read()
        return json.loads(string)
