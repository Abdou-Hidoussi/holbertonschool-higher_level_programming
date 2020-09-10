#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in range(len(matrix)):
        col = []
        for j in range(len(matrix[i])):
            col.append(matrix[i][j] * matrix[i][j])
        new.append(col)
    return new
