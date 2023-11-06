#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        for i in range(len(row)):
            if i < len(row) - 1:
                print(row[i], end=" ")
            else:
                print(row[i])
    print()
