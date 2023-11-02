#!/usr/bin/python3

if __name__ == '__main__':
    """Print the number of and list of arguments."""
    import sys
    argc = len(sys.argv) - 1
    argv = sys.argv

    if argc == 0:
        print("{:d} arguments.".format(argc))
    elif argc == 1:
        print("{:d} arguments:".format(argc))
    else:
        print("{:d} arguments:".format(argc))
    for x in range(argc):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
