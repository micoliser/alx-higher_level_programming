#!/usr/bin/python3
"""
    This module contains a function that returns a list of lists
    of integers representing the pascals triangle of n
"""


def pascal_triangle(n):
    """ Returns a list representing pascals triangle """

    tri_list = []
    if n <= 0:
        return tri_list

    tri_list.append([1])
    if n == 1:
        return tri_list

    tri_list.append([1, 1])
    if n == 2:
        return tri_list

    for i in range(2, n):
        row = [1]
        prev_row = tri_list[i - 1]

        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])

        row.append(1)
        tri_list.append(row)

    return tri_list
