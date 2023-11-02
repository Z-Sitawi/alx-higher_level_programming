#!/usr/bin/python3

if __name__ == '__main__':
    """Print the number of and list of arguments."""
    import sys
    argc = len(sys.argv) - 1
    argv = sys.argv
    count = 0

    if argc == 0:
        print("{:d} arguments.".format(argc))
    elif argc == 1:
        print("1 arguments:")
    else:
        print("{:d} arguments:".format(argc))
    for x in argv:
        if x not in argv[0]:
            count = count + 1
            print("{:d}: {:s}".format(count, x))
