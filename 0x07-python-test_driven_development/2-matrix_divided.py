#!/usr/bin/python3
"""
matrix_divided - divides all elements of a matrix.

matrix must be a list of lists of integers or floats, otherwise raise a TypeError
exception with the message matrix must be a matrix (list of lists) of integers/floats
Each row of the matrix must be of the same size, otherwise raise a TypeError
exception with the message Each row of the matrix must have the same size
div must be a number (integer or float), otherwise raise a TypeError
exception with the message div must be a number
div can’t be equal to 0, otherwise raise a ZeroDivisionError
exception with the message division by zero
All elements of the matrix should be divided by div, rounded to 2 decimal places
Returns a new matrix
You are not allowed to import any module
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): Matrix of integers or floats.
        div (int or float): Number to divide the matrix elements by.

    Returns:
        list of lists: New matrix with elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists, if any row is not the
                   same size, or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return result_matrix
if __name__ == "__main__":
    import doctest
    doctest.testfile('./tests/2-matrix_divided.txt', globals=globals())
