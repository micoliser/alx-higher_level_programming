#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)

    if length == 0:
        first_c = None
    else:
        first_c = sentence[0]

    new_tuple = (length, first_c)

    return new_tuple
