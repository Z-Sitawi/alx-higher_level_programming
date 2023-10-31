#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase."""
    for c in str:
        if 97 <= ord(c) <= 122:  # if lowercase
        c = chr(ord(c) - 32)  # get ascii of upper & turn it to char
        print("{}".format(c), end="")
    print("")
