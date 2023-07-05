#!/usr/bin/python3
import numpy as np
"""
Function that multiplies 2 matrices by using the module NumPy
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b using the NumPy module.

    """

    try:
        result = np.dot(m_a, m_b)
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
