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
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Return Square area """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.size == 0:
            print("")
        for x in range(self.size):
            for y in range(self.size):
                print("#", end="")
            print('')


my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")