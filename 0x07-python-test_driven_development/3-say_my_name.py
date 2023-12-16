#!/usr/bin/python3
"""Defines a function that prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """

    :param first_name: the firs name
    :param last_name: the lastname

    :raises TypeError: if first_name and last_name are not strings
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    elif type(last_name) is not str:
        raise TypeError('last_name must be a string')

    if last_name == "":
        print("My name is {:s} ".format(first_name))
    elif last_name != "":
        print("My name is {:s} {:s}".format(first_name, last_name))
