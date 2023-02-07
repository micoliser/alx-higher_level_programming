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

        rtrv_all = True
        if type(attrs) is list:
            for item in attrs:
                if type(item) != str:
                    rtrv_all = True
                else:
                    rtrv_all = False

        if not rtrv_all:
            return {key: self.__dict__[key] for key in
                    attrs if key in self.__dict__}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the instance"""

        for key, val in json.items():
            print("{}: {}".format(key, val))
            setattr(self, key, val)
