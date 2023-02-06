#!/usr/bin/python3
"""
    This module contains a class MyList that inherits from the list class.
    it has a method print_sorted() that prints out the list in sorted order
"""


class MyList(list):
    """ A class inherited from te list class """

    def print_sorted(self):
        """ prints out the list in sorted order """

        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
