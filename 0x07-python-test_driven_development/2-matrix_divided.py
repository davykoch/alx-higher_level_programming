#!/usr/bin/python3
"""
matrix_divided - divides all elements of a matrix.

matrix must be a list of lists of integers or floats
Each row of the matrix must be of the same size, otherwise raise a TypeError
exception with the message Each row of the matrix must have the same size
div must be a number (integer or float), otherwise raise a TypeError
exception with the message div must be a number
div can’t be equal to 0, otherwise raise a ZeroDivisionError
exception with the message division by zero
All elements of the matrix should be divided by div
Returns a new matrix
You are not allowed to import any module
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Args:
        matrix (list of lists): The matrix to divide.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with each element divided by the divisor.

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   if each row of the matrix does not have the same size,
                   or if the divisor is not a number.
        ZeroDivisionError: If the divisor is 0.

    Example:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """
    if not matrix or not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError
                ("matrix must be a matrix(list of lists)of integers / floats")
            new_row.append(round(element / div, 2))
        result_matrix.append(new_row)

    return result_matrix
