#!/usr/bin/python3
""" A function that prints a text with 2 new lines
    after each of these characters: (.) (?) (:)
"""


def text_indentation(text):
    """

    :param text: (str) text to print.
    :raise TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    modified_text = ""
    for i, char in enumerate(text):
        if char in ['?', ':', '.']:
            modified_text += char + "\n\n"
        else:
            modified_text += char

    print(modified_text.replace("\n\n ", "\n\n"), end="")
