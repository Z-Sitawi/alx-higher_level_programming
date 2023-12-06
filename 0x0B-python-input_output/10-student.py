#!/usr/bin/python3
""" Define a class named 'Student' """


class Student:
    """ represents a students by
        first_name, last_name, and age
    """

    def __init__(self, first_name, last_name, age):
        """ Initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance """
        if (isinstance(attrs, list)
                and all(isinstance(element, str) for element in attrs)):
            dic = {}
            for k in attrs:
                if hasattr(self, k):
                    dic[k] = getattr(self, k)
            return dict(sorted(dic.items()))
        else:
            dic = self.__dict__
            return dict(sorted(dic.items()))
