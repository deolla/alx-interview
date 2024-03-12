#!/usr/bin/python3
"""Prime game."""


def isWinner(num_rounds, num_list):
    """Determine the winner of a prime game session with given rounds.

    Args:
        num_rounds (int): Number of rounds.
        num_list (list): List of round limits.

    Returns:
        str or None: Name of the winner or None if undetermined.
    """
    if num_rounds < 1 or not num_list:
        return None
    maria_score, ben_score = 0, 0
    max_num = max(num_list)
    primes = [True for _ in range(1, max_num + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, max_num + 1, i):
            primes[j - 1] = False
    for _, n in zip(range(num_rounds), num_list):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        ben_score += primes_count % 2 == 0
        maria_score += primes_count % 2 == 1
    if maria_score == ben_score:
        return None
    return 'Maria' if maria_score > ben_score else 'Ben'
