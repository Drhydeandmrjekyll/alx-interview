#!/usr/bin/env python3
"""
Script defines method minOperations(n) that calculates fewest number
of operations needed to result in exactly n 'H' characters in a
text file. The two allowed operations are Copy All and Paste.

If n is impossible to achieve,method returns 0.
"""


def minOperations(n):
    """Calculate Minimum Operations"""
    if not isinstance(n, int) or n <= 1:
        return 0
    b = 1
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            b = (i if i != 0 else 1)
            break
    z = int((minOperations(b) if b != 1 else 0) + n / b)
    return z