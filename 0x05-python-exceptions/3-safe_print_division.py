#!/usr/bin/python3
def safe_print_division(a, b):
    """  divides 2 integers and prints the result """
    result = float()
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
        return "None"
    finally:
        if result is not None:
            print("Inside result: {:.1f}".format(result))
        else:
            print("Inside result: {:s}".format("None"))
