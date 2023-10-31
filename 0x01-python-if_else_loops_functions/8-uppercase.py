#!/usr/bin/python3
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
