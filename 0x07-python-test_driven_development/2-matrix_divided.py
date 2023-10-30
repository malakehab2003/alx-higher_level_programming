#!/usr/bin/python3
""" matrix divide """


def matrix_divided(matrix, div):
    new_mat = []
    if len(matrix) == 0:
        return new_mat
    l = len(matrix[0])
    for i in range(len(matrix)):
        if l != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int and type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    element = 0
    for i in range(len(matrix)):
        element = list(map(lambda x: round(x / div, 2), matrix[i]))
        new_mat.append(element)

    return new_mat
