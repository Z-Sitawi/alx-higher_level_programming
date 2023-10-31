#!/usr/bin/python3
def remove_char_at(str, n):
    # Check if the index is valid
    len_str = len(str)
    if n < 0 or n >= len_str:
        return str

    str_copy = ""

    for i in range(len_str):
        if i != n:
            str_copy += str[i]

        return str_copy
