#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """ Represent a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ :return: the rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ :return: the rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        for y in range(self.height):
            for x in range(self.width):
                print(self.print_symbol, end="")
            print("", end="\n" if y < self.height - 1 else "")
        return ""

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({str(self.__width)}, {str(self.__height)})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
