#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first_tuple = tuple_a[:2] + (0, 0)
    second_tuple = tuple_b[:2] + (0, 0)
    sum_tuple = (
        first_tuple[0] + second_tuple[0],
        first_tuple[1] + second_tuple[1]
    )
    return sum_tuple
