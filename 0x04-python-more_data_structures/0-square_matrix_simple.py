#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return None
    else:
        matrix_sq = [[x ** 2 for x in row] for row in matrix]
        return matrix_sq
