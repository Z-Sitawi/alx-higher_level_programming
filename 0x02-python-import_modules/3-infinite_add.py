#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of and list of int arguments."""
    import sys

    argv = sys.argv
    total = 0

    for x in argv:
        if x != argv[0]:
            total = total + int(x)
    print("{:d}".format(total))
