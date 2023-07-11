#!/usr/bin/python3
"""Pascal's Triangle module"""


def pascal_triangle(n):
    """Returns list of lists of integers representing the Pascal’s triangle"""
    if n <= 0:
        return []

    triangle = [[1]]

    for row_num in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]

        for column_index in range(1, len(prev_row)):
            current_value = prev_row[column_index-1] + prev_row[column_index]
            current_row.append(current_value)

        current_row.append(1)
        triangle.append(current_row)

    return triangle
