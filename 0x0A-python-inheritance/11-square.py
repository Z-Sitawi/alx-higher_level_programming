#!/usr/bin/python3
""" Defines a class Square that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represent a Square using Rectangle."""
    def __init__(self, size):
        """
            Initialize a Square
        :param size: size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ calculates the area of a square """
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
