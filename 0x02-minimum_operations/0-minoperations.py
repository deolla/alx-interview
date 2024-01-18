#!/usr/bin/env python3
"""Write a method that calculates the fewest number of operations needed."""


def minOperations(n):
    """Returns the fewest number of operations needed."""
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(int(n / i)) + i
