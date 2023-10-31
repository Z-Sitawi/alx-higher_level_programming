#!/usr/bin/python3
def remove_char_at(str, n):
    """Create a copy of the string without the character at position n."""

    if not 0 < n:  # Check if the index is valid
        return str
    return str[:n] + str[n+1:]
