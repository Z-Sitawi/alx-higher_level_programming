#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout

    :param filename: the name if the text file to read from
    :return: Nothing
    """
    with open(filename, "r", encoding="utf-8") as file:
        read = file.read()
        print(read)
