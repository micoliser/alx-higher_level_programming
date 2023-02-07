#!/usr/bin/python3
"""
    This module contains a function that appends a string to a text file
    and return the number of characters written
"""


def append_write(filename="", text=""):
    """ Appends the characters in text to filename """

    with open(filename, "a", encoding="UTF-8") as f:
        return (f.write(text))
