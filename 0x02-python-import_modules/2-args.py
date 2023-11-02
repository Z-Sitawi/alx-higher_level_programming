#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    print("argc", argc)
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))
    for x in range(argc):
        print("{:d}: {:s}".format(x + 1, sys.argv[x + 1]))
