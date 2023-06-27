#!/usr/bin/env python

def magic_calculation(a, b):
    result = 0

    for index in range(1, 4):
        try:
            if index > a:
                raise ValueError("Too far")
            result += (a ** b) / index
        except ValueError:
            result = b + a
            break

    return round(result, 2)
