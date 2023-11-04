#!/usr/bin/python3
def multiple_returns(sentence):
    """ returns a tuple with the length of a string and its first char """
    str_len = len(sentence)
    if sentence is None or sentence == "":
        return 0, None
    else:
        return str_len, sentence[0]
