#!/usr/bin/python3
""" Defines a class which will be the “base” of
    all the other classes in this project
"""


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
