#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ prints a matrix of integers """
    for x in matrix:
        for i in range(len(x)):
            print("{:d}".format(x[i]), end=" " if i != len(x) - 1 else "")

        print("")
