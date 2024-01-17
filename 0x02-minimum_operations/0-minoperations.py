#!/usr/bin/python3
"""
Module to get min operations
"""


def minOperations(n):
    """
    Calculate Minimum Operations.
    """
    if not isinstance(n, int) or n <= 1:
        return 0
    b = 1
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            b = (i if i != 0 else 1)
            break
    z = int((minOperations(b) if b != 1 else 0) + n / b)
    return z
