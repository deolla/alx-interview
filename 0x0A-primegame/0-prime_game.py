#!/usr/bin/python3
"""Prime Game."""


def generate_primes(limit):
    """Generate a list of prime numbers."""
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    return [num for num, is_prime in enumerate(primes) if is_prime]


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def play_round(n):
    """Play a round of the prime game."""
    primes = generate_primes(n)
    player = 'Maria'

    while True:
        valid_moves = [prime for prime in primes if prime <= n]
        
        if not valid_moves:
            return 'Ben' if player == 'Maria' else 'Maria'
        
        if player == 'Maria':
            chosen_num = min(valid_moves)
        else:
            chosen_num = max(valid_moves)

        primes = [num for num in primes if num % chosen_num != 0]
        n -= chosen_num
        player = 'Ben' if player == 'Maria' else 'Maria'

def isWinner(x, nums):
    maria_wins = ben_wins = 0

    for n in nums:
        primes = generate_primes(n)
        prime_count = len(primes)

        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
    
