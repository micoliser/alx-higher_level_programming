#!/usr/bin/python3
"""
    This module contains a function that reads a text file and prints to
    stdout
"""


def read_file(filename=""):
    """ Reads a text from a file and prints to stdout """

    with open(filename, "r", encoding="UTF-8") as f:
        text = f.read()
        print(text, end="")
