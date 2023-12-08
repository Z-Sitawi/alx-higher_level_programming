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
    with open(filename, "r+", encoding="utf-8") as file:
        lines = file.readlines()
        new_lines = []

        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string + "\n")

        # Go back to the beginning of the file before writing
        file.seek(0)
        file.writelines(new_lines)
        # Remove any remaining content from the old file, if necessary
        file.truncate()