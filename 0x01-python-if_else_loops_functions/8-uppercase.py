#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if 97 <= ord(c) <= 122:  # if lowercase
        c = chr(ord(c) - 32)  # get ascii of upper & turn it to char
        print("{}".format(c), end="")
    print("")

# while loop version
"""
def uppercase(str):
    i = 0
    s = ""
    while i < len(str):
        c = str[i]
        if 97 <= ord(c) <= 122:  # if lowercase
            ac = ord(c) - 32  # get ascii of uppercase
            c = chr(ac)  # turn ascii to character
            s = s + c  # add character to string.
        else:
            s = s + c
            i += 1

    print("{:s}".format(s))
"""
