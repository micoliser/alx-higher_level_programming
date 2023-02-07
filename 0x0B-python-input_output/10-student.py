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

    def to_json(self, attrs=None):
        """ Retrieves the dictionary representation of the instance """

        if type(attrs) is list:
            for item in attrs:
                if type(item) != str:
                    return self.__dict__

            return {key: self.__dict__[key] for key in
                    attrs if key in self.__dict__}

        return self.__dict__
