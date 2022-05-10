#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            value = matrix[x][y]
            new_matrix[x][y] = [x**2][y**2]
    return new_matrix
