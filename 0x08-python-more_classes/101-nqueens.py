#!/usr/bin/python3
import sys
"""
The N queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard.
"""


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check for queens in the same column
    for r in range(row):
        if board[r] == col:
            return False

    # Check for queens in the upper diagonal
    for r, c in enumerate(board[:row]):
        if c == col + row - r or c == col - row + r:
            return False

    return True


def solve_n_queens(board, row):
    """
    Recursive function to solve the N Queens puzzle
    """
    if row == N:
        # Found a solution, print it
        print([[r, c] for r, c in enumerate(board)])

    for col in range(N):
        if is_safe(board, row, col):
            # Place the queen
            board[row] = col

            # Recur to place the rest of the queens
            solve_n_queens(board, row + 1)

            # Backtrack and remove the queen
            board[row] = -1


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty chessboard
    board = [-1] * N

    # Solve the N Queens puzzle
    solve_n_queens(board, 0)
