#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    len1 = len(tuple_a)
    len2 = len(tuple_b)

    if len1 >= 2:
        first_idx_a = tuple_a[0]
        second_idx_a = tuple_a[1]
    elif len1 == 1:
        first_idx_a = tuple_a[0]
        second_idx_a = 0
    elif len1 == 0:
        first_idx_a = 0
        second_idx_a = 0

    if len2 >= 2:
        first_idx_b = tuple_b[0]
        second_idx_b = tuple_b[1]
    elif len2 == 1:
        first_idx_b = tuple_b[0]
        second_idx_b = 0
    elif len2 == 0:
        first_idx_b = 0
        second_idx_b = 0

    tuple_add = (first_idx_a + first_idx_b, second_idx_a + second_idx_b)

    return tuple_add
