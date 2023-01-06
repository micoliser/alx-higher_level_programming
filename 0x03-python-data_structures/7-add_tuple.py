#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    len1 = len(tuple_a)
    len2 = len(tuple_b)

    if len1 >= 2:
        first_index_a = tuple_a[0]
        second_index_a = tuple_a[1]
    elif len1 == 1:
        first_index_a = tuple_a[0]
        second_index_a = 0
    elif len1 == 0:
        first_index_a = 0
        second_index_a = 0

    if len2 >= 2:
        first_index_b = tuple_b[0]
        second_index_b = tuple_b[1]
    elif len2 == 1:
        first_index_b = tuple_b[0]
        second_index_b = 0
    elif len2 == 0:
        first_index_b = 0
        second_index_b = 0

    tuple_add = (first_index_a + first_index_b, second_index_a + second_index_b)

    return tuple_add
