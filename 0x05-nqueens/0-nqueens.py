#!/usr/bin/python3
"""N queens problem"""
import sys


def is_safe(board, row, col, N):
    """Check if a queen can be placed on board[row][col]"""
    # Check if there is a queen in the same column
    for i in range(row):
        if (
            (board[i] == col)
            or (board[i] - i == col - row)
            or (board[i] + i == col + row)
        ):
            return False
    return True


def solve_nqueens(board, row, N):
    """Solve N queens problem"""
    if row == N:
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(board, row + 1, N)


def print_solution(board):
    """Print the solution"""
    print([list(map(int, [i, board[i]])) for i in range(len(board))])


def nqueens(N):
    """N queens problem"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0] * N
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
