#!/usr/bin/python3
""" Defines a function that inserts a line of text to a file,
    after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """

    :param filename: (str) the name of text file
    :param search_string: (str) string to look for
    :param new_string: (str) string to insert
    :return: nothing
    """
    new_lines = ""
    with open(filename, encoding="utf-8") as file:

        for line in file:
            new_lines += line
            if search_string in line:
                new_lines += new_string

    with open(filename, "w", encoding="utf-8") as file:
        file.write(new_lines)
