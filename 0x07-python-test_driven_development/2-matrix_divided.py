#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ divides all elements of a matrix.

    Args:
        matrix: A list of lists of integers or floats.
        div: the divisor

        Returns a new matrix with the divided elements
    """

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0]) if matrix else 0  # Size of first row

    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if row_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    rows = []
    for row in matrix:
        for elm in row:
            d = elm / div
            rows.append(round(d, 2))
        rc = rows.copy()
        new_matrix.append(rc)
        rows.clear()

    return new_matrix
