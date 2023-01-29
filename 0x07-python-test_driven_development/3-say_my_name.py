#!/usr/bin/python3
"""
    This module contains a function
    say_my_name(first_name, last_name) that prints
    My name is <first name> <last name>
    first name and last name must be a string, otherwise a
    TypeError is raised
"""


def say_my_name(first_name, last_name=""):
    """ Prints a name """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
