#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == "":
        return 0
    romannum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    dec = 0
    roman_string.upper()
    for x in roman_string:
        if x in romannum:
            dec = dec + romannum[x]
    return dec
