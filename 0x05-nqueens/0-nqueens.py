#!/usr/bin/python3
"""Write a program that solves the N queens problem."""
import sys


def backtrack(r, n, pop, pos, neg, board):
    """A program that solves the N queens problem."""
    if r == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for h in range(n):
        if h in pop or (r + h) in pos or (r - h) in neg:
            continue

        pop.add(h)
        pos.add(r + h)
        neg.add(r - h)
        board[r][h] = 1

        backtrack(r + 1, n, pop, pos, neg, board)

        pop.remove(h)
        pos.remove(r + h)
        neg.remove(r - h)
        board[r][h] = 0


def nqueens(n):
    """
    The program should print every possible solution to
    the problem One solution per line.
    """
    pop = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, pop, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
