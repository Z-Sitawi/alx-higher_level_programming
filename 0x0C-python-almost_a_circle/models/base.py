#!/usr/bin/python3
""" Defines a class which will be the “base” of
    all the other classes in this project
"""
import ex


class Base:
    """ Represents a base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initiates a base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts

        :param list_dictionaries: is a list of dictionaries
        :return: the string: "[]" If list_dictionaries is None or empty,
        Otherwise, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes the JSON string representation of list_objs to a file.
            It overwrites the file if it already exists

        :param list_objs: is a list of instances who inherits of Base
                (example: list of Rectangle or list of Square instances)

        If list_objs is None, save an empty list.
        The filename must be: <Class name>.json - example: Rectangle.json
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        :param json_string: A JSON str representation of a list of dicts.
        :returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
