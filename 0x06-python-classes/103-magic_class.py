#!/usr/bin/python3
import math


class MagicClass:
    """ Represent a circle """
    def __init__(self, radius=0):
        """
            Initialize a MagicClass.

            Arg:
               radius (float or int): The radius of the new circle.
       """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ Return the area of the circle """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Return The circumference of the circle"""
        return 2 * math.pi * self.__radius
