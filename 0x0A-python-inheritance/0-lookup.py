#!/usr/bin/python3
"""Defines an object available attribute lookup function."""


def lookup(obj):
    """
    :param obj: An object.
    :return: the list of available attributes and methods of an object
    """

    return dir(obj)
