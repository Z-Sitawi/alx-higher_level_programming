#!/usr/bin/python3
""" Defines a class 'MyList' that inherits from 'list' """


class MyList(list):
    """ Defines a list """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        self.sort()
        print(self)
