#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new = []
    for i in range(len(matrix)):
        new_row = list(map(lambda x: x ** 2, matrix[i]))
        new.append(new_row)
    return new
