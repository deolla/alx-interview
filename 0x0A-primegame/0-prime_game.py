#!/usr/bin/python3
"""Prime Game."""


def isWinner(x, nums):
    """Determines the winner of each game, returns the name of the player."""
    def sieve(n):
        """Implements the Sieve of Eratosthenes algorithm."""
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return primes

    def playGame(n):
        """Simulates the game for a given value of n."""
        primes = sieve(n)
        turn = 0  # 0 for Maria, 1 for Ben
        while True:
            if all(not primes[i] for i in range(2, n + 1)):
                return turn
            for i in range(2, n + 1):
                if primes[i]:
                    for j in range(i, n + 1, i):
                        primes[j] = False
                    turn = 1 - turn

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = playGame(n)
        if winner == 0:
            maria_wins += 1
        elif winner == 1:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
