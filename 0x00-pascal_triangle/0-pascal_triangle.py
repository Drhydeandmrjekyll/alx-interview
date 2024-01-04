#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
    - n: An integer representing the number of rows in Pascal's triangle.

    Returns:
    - A list of lists representing Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]  # First element in each row is always 1

        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)  # Last element in each row is always 1
        triangle.append(row)

    return triangle
