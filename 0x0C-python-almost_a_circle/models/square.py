#!/usr/bin/python3
""" Defines a class named Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Represent a square """
    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes a square
        parameters:
            :param width (int): The width of the new Rectangle.
            :param height (int): The height of the new Rectangle.
            :param x (int): The x coordinate of the new Rectangle.
            :param y (int): The y coordinate of the new Rectangle.
            :param id (int): The identity of the new Rectangle.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """

        :return: [Square] (<id>) <x>/<y> - <size>
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}")
