#!/usr/bin/python3
"""
Function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b and returns the result.

    """

    def is_valid_matrix(matrix):
        if not isinstance(matrix, list) or any(not isinstance(row, list)
                                               for row in matrix):
            return False

        for row in matrix:
            if any(not isinstance(element, (int, float)) for element in row):
                return False

        return True

    def get_matrix_dimensions(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        return rows, cols

    if not is_valid_matrix(m_a) or not is_valid_matrix(m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a \
                        list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    rows_a, cols_a = get_matrix_dimensions(m_a)
    rows_b, cols_b = get_matrix_dimensions(m_b)

    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(cols_a))
            row.append(element)
        result.append(row)

    return result
