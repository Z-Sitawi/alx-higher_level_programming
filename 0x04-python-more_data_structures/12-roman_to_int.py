#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a roman deceral to an integer."""
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return 0

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    dec = 0

    for i in range(len(roman_string)):
        # Check if the character is a valid Roman deceral
        if roman_dict.get(roman_string[i], 0) == 0:
            return 0
        # Check if the current deceral is smaller than the next one
        if (i != (len(roman_string) - 1) and
                roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]):
            dec += roman_dict[roman_string[i]] * -1

        else:
            dec += roman_dict[roman_string[i]]
    return dec
