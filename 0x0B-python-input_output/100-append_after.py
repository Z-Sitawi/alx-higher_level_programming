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
    with open(filename, "r", encoding="utf-8") as file:
        read = file.read()
        mylist = []
        line = ""
        new_lines = ""

        for i in read:
            if i != "\n":
                line += i[:]
            else:
                mylist.append(line)
                line = ""
            mylist.append(line)
        for x in mylist:
            if search_string in x:
                new_lines += x + "\n" + new_string + "\n"
            else:
                new_lines += x + "\n"
        new_lines = new_lines[: len(new_lines) - 1]
    with open(filename, "w", encoding="utf-8") as file:
        file.write(new_lines)
