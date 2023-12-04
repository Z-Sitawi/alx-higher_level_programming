#!/usr/bin/python3
""" Defines a class 'BaseGeometry' """


class BaseGeometry:
    """ Represent a base geometry """
    def area(self):
        """ raises an Exception with a specified msg"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ It validates a value

        :param name: we assume it is always a string.
        :param value: the value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
