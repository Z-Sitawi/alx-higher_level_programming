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

    def to_json(self):
        """ retrieves a dictionary representation of a Student instance """
        return self.__dict__
