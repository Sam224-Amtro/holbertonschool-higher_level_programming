#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for k in range(len(row)):
            print("{:d}".format(row[k]), end="")
            if k < len(row) - 1:
                print(" ", end="")
        print()
