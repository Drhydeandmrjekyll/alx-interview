#!/usr/bin/env python3
"""
Script defines method minOperations(n) that calculates fewest number
of operations needed to result in exactly n 'H' characters in a
text file. The two allowed operations are Copy All and Paste.

If n is impossible to achieve,method returns 0.
"""


def minOperations(n):
    if n <= 0:
        return 0

    operations = 0
    clipboard = 1

    while clipboard < n:
        if n % clipboard == 0:
            clipboard = n // clipboard
            operations += 2
        else:
            clipboard += clipboard
            operations += 1

    return operations
