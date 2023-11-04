#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ prints a matrix of integers """
    for x in matrix:
        for i in x:
            print("{:d}".format(i), end=" ")
        print("")
