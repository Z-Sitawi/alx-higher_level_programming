#!/usr/bin/python3
def roman_to_int(roman_string):
    """ converts a Roman numeral to an integer """
    if (not isinstance(roman_string, str)
            or roman_string is None):
        return 0

    romannum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    dec = 0

    for i in range(len(roman_string)):
        # Check if the character is a valid Roman numeral
        if romannum.get(roman_string[i], 0) == 0:
            return 0

    for x in roman_string:
        if x in romannum:
            dec = dec + romannum[x]
    return dec
