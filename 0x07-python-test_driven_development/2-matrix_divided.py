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
        matrix (list): List of lists containing integers/floats.
        div (int/float): The divisor.

    Returns:
        list: New matrix with all elements divided by div.

    Raises:
        TypeError: If the matrix contains non-numeric elements.
        TypeError: If the matrix rows are of different sizes.
        ZeroDivisionError: If div is 0.
    """

    if not isinstance(
        matrix,
        list) or not all(
        isinstance(
            row,
            list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(element / div, 2)
                      for element in row] for row in matrix]
    return result_matrix

