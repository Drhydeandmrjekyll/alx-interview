#!/usr/bin/python3
"""
Module to get min operations method minOperations(n) t
hat calculates the fewest number of operations needed to
result in exactly n 'H' characters in a text file. The two
allowed operations are Copy All and Paste.
"""


def minOperations(n):
    """
    Calculate Minimum Operations.
    """
    if not isinstance(n, int) or n <= 1:
        return 0
    b = 1
    i = n - 1
    while i > 0:
        if n % i == 0:
            b = (i if i != 0 else 1)
            break
        i -= 1
    z = int((minOperations(b) if b != 1 else 0) + n / b)
    return z
