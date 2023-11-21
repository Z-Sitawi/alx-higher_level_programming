#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """ Represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
            self.__size = size
            self.__position = position
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2 and all(isinstance(x, int) for x in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Return Square area """
        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.size == 0:
            print("")
            return
        for y in range(self.__position[1]):
            print("")
        for j in range(self.size):
            for x in range(self.position[0]):
                print(" ", end="")
            for y in range(self.size):
                print("*  ", end="")
            print('')
