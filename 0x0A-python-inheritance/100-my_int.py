#!/usr/bin/python3
"""Defines a class 'MyInt' that inherits from 'int' """


class MyInt(int):
    """ Inverts == and != operators """

    def __eq__(self, other):
        """ reverts == to !=
        :param other: an integer
        """
        return self.real != other

    def __ne__(self, other):
        """ reverts != to ==
        :param other: an integer
        """
        return self.real == other
