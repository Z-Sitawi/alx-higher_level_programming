#!/usr/bin/python3
""" Defines a class 'BaseGeometry' and
    a class Rectangle that inherits from BaseGeometry
"""


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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        if width <= 0 or type(width) != int:
            Rectangle.integer_validator(self, "width", width)

        if height <= 0 or type(height) != int:
            Rectangle.integer_validator(self, "height", height)

        self.__width = width
        self.__height = height
