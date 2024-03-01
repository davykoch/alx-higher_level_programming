#!/usr/bin/python3
"""
This module contains a function to find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]


if __name__ == "__main__":
    test_cases = [
        [1, 2, 4, 6, 3],
        [4, 2, 1, 2, 3, 1],
        [2, 2, 2],
        [],
        [-2, -4, 2, 1],
        [4, 2, 1, 2, 2, 2, 3, 1]
    ]

    for test_case in test_cases:
        print(find_peak(test_case))
