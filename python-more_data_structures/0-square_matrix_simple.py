#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return [[]]
    elif not matrix or all(not row for row in matrix):
        return [[]]
    else:
        new_matrix = []
        for row in matrix:
            new_row = []
            for num in row:
                new_row.append(num ** 2)
            new_matrix.append(new_row)
        return new_matrix
