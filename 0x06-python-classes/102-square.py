#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ Represent a square"""
    def __init__(self, size=0):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__size = value
        else:
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        return False

    def __ne__(self, other):
        if self.area() != other.area():
            return True
        return False

    def __gt__(self, other):
        if self.area() > other.area():
            return True
        return False

    def __ge__(self, other):
        if self.area() >= other.area():
            return True
        return False

    def __lt__(self, other):
        if self.area() < other.area():
            return True
        return False

    def __le__(self, other):
        if self.area() <= other.area():
            return True
        return False
