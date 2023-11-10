#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Computes the square value of all integers of a matrix.
    new_matrix = matrix[:]
    return [list(map(lambda x: x * x, sec)) for sec in new_matrix]
