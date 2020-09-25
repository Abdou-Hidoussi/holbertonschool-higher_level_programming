#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
        return

    if div == 0:
        raise ZeroDivisionError("division by zero")
        return

    if not isinstance(matrix, list) or matrix == [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        return
    for x in matrix:
        if not isinstance(x, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            return
        if len(x) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
            return
        for i in x:
            if not isinstance(i, (float, int)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                return

    new = []
    for x in matrix:
        newx = []
        for y in x:
            newx.append(round((y / div), 2))
        new.append(newx)
    return new

    

