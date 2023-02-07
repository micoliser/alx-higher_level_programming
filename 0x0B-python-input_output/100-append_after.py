#!/usr/bin/python3
"""
    This module contains a function that inserts a line of text into a file
    after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of new string after the line containing search string
    """

    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)

        if line.find(search_string) != -1:
            new_lines.append(new_string)

    with open(filename, "w", encoding="UTF-8") as f:
        f.writelines(new_lines)
