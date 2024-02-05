#!/usr/bin/python3
"""N queens module"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_nqueens_util(board, col, n, res):
    """
    A recursive utility function to solve N Queens problem
    """
    # Base case: If all queens are placed then return True
    if col == n:
        res.append([[i, row.index(1)] for i, row in enumerate(board)])
        return True

    # Initialize result
    found_solution = False

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of queens
            found_solution = solve_nqueens_util(board, col + 1, n, res) or found_solution

            # If placing queen in board[i][col] doesn't lead to a solution
            # then remove queen from board[i][col]
            board[i][col] = 0

    # if queen can not be place in any row in this column col return False
    return found_solution


def solve_nqueens(n):
    """
    The main function to solve N Queens problem
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize board
    board = [[0 for _ in range(n)] for _ in range(n)]

    res = []
    if not solve_nqueens_util(board, 0, n, res):
        print("No solution exists")
        return

    for solution in res:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
