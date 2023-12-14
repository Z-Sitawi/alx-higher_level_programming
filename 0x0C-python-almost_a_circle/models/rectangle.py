#!/usr/bin/python3
""" Defines a class named Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Represent a Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes a Rectangle
        parameters:
            :param width (int): The width of the new Rectangle.
            :param height (int): The height of the new Rectangle.
            :param x (int): The x coordinate of the new Rectangle.
            :param y (int): The y coordinate of the new Rectangle.
            :param id (int): The identity of the new Rectangle.

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area value of the Rectangle instance.

        :return: the area value of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
                    prints in stdout
        the Rectangle instance with the character '#'
        """
        for y in range(self.y):
            print("")
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """

        :return: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}/{self.height}")

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
                self.height = args[2]
            elif len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            elif len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        else:
            for k in kwargs.keys():
                if k == "id":
                    self.id = kwargs[k]
                elif k == "x":
                    self.x = kwargs[k]
                elif k == "y":
                    self.y = kwargs[k]
                elif k == "width":
                    self.width = kwargs[k]
                elif k == "height":
                    self.height = kwargs[k]
