#!/usr/bin/python3
def magic_calculation(a, b, c):
    for _ in range(3):
        if a < b:
            return c
        elif b > c:
            return a + b
        else:
            return a * b - c
