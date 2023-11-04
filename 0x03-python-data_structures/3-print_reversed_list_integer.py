#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    start = 0
    end = len(my_list) - 1

    while start < end:
        # Swap the elements at start and end indices
        my_list[start], my_list[end] = my_list[end], my_list[start]
        start += 1
        end -= 1

    for x in my_list:
        print("{:d}".format(x))
