#!/usr/bin/python3


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the specified number of rows.

    Parameters:
    - n (int): The number of rows for Pascal's triangle.

    Returns:
    - list of lists: A list of lists representing Pascal's triangle.
      Each inner list corresponds to a row in the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
