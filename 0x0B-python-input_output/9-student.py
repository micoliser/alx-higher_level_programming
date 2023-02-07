#!/usr/bin/python3
"""
    This module contains a Student class
"""


class Student:
    """ A student class """

    def __init__(self, first_name, last_name, age):
        """ Initializes self """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrieves the dictionary representation of the instance """

        return (self.__dict__)
