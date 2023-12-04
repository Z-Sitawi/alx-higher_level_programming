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

        :return: if value is not an integer: raise a TypeError exception,
                    with the message <name> must be an integer
                 if value is less or equal to 0: raise a ValueError exception
                    with the message <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
