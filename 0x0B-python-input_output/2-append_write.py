#!/usr/bin/python3
""" A function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
"""


def append_write(filename="", text=""):
    """

    :param filename: the text file to append to.
    :param text: the text to append
    :return: the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
