#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list) - 1:
        for x in range(len(my_list)):
            if x == idx:
                del my_list[x]
                return my_list
    return my_list
