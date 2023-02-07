#!/usr/bin/python3
"""
    This module contains a function that writes a string to a text file and
    return the number of characters written
"""


def write_file(filename="", text=""):
    """ Writes the characters in text to filename """

    with open(filename, "w", encoding="UTF-8") as f:
        return (f.write(text))
