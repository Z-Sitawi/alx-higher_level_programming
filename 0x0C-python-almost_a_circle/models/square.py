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

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """ set the size of the Square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            Assigns an argument to each attribute
        :param args: N number of arguments
        :param kwargs: N number of key/value arguments
        """
        if args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            elif len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for k in kwargs.keys():
                if k == "id":
                    self.id = kwargs[k]
                elif k == "x":
                    self.x = kwargs[k]
                elif k == "y":
                    self.y = kwargs[k]
                elif k == "size":
                    self.width = kwargs[k]
