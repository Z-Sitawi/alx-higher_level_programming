#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        ld = number % 10
        print("{:d}".format(ld), end="")
        return ld
    elif number < 0:
        ld = -number % 10
        print("{:d}".format(ld), end="")
        return ld
    else:
        ld = 0
        print("{:d}".format(ld), end="")
        return ld
