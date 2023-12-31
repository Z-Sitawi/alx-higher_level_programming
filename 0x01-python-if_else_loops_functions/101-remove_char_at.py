#!/usr/bin/python3
def remove_char_at(str, n):
    """Create a copy of the string without the character at position n."""

    if n < 0 or n >= len(str):  # Check if the index is valid
        return str
    return str[:n] + str[n+1:]
