#!/usr/bin/python3
""" Defines a class which will be the “base” of
    all the other classes in this project
"""
import json


class Base:
    """ Represents a base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initiates a base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """

        :param list_dictionaries: is a list of dictionaries
        :return: the string: "[]" If list_dictionaries is None or empty,
        Otherwise, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)
