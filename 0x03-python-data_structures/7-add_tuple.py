#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = [0, 0]

    for i in range(2):
        if len(tuple_a) > i:
            result[i] += tuple_a[i]
        if len(tuple_b) > i:
            result[i] += tuple_b[i]

    return tuple(result)
