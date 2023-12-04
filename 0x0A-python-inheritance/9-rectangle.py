#!/usr/bin/python3
""" Defines a class Rectangle that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            :param width (int): The width of the new Rectangle.
            :param height (int):  The height of the new Rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ calculates the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
