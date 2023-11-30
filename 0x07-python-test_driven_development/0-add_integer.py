#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):
	"""add integers a and b with conditions
	must be integers or floats
	must be first casted to integers if they are float
	"""
	if not isinstance(a, (int, float)) or a is None:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
