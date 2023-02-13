#!/usr/bin/python3
"""
    This module contains a function print_square(size)
    that prints a square with characters # based on size
    if size is not an integer or size is less than 0, a
    TypeError is raised
"""


def print_square(size):
    """ Prints a square with # character """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
