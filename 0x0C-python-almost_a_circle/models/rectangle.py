#!/usr/bin/python3
""" Defines a class named Rectangle """
Base = __import__("base").Base


class Rectangle(Base):
    """ Represent a Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initiates a Rectangle """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
