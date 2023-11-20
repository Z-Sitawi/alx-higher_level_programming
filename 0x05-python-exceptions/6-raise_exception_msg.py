#!/usr/bin/python3
def raise_exception_msg(message=""):
    """ raises a name exception with a message """
    print("{:s}".format(message))
    raise NameError
