#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for index in range(1, 3):
        try:
            if index > a:
                raise ValueError("Too far")
            else:
                result += (a ** b) / index
        except ValueError:
            result = b + a
            break
    return result
