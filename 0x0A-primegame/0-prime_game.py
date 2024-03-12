#!/usr/bin/python3
"""Prime Game."""


def isWinner(x, nums):
    """
    Determine the winner of each game.

    Args:
    - x: Number of rounds.
    - nums: List of integers representing the upper bounds for each round.

    Returns:
    - Name of the player that won the most rounds.
    - If the winner cannot be determined, return None.
    """
    def is_prime(num):
        """
        Check if a number is prime.

        Args:
        - num: The number to check.

        Returns:
        - True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes_up_to_n(n):
        """
        Get a list of prime numbers up to a given value.

        Args:
        - n: The upper bound for prime numbers.

        Returns:
        - List of prime numbers.
        """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def can_remove_number(nums, num):
        """
        Check if a given number and its multiples can be removed from the list.

        Args:
        - nums: The list of numbers.
        - num: The number to check.

        Returns:
        - True if the number can be removed, False otherwise.
        """
        for i in range(num, len(nums), num):
            if nums[i] != -1:
                return True
        return False

    def remove_multiples(nums, num):
        """
        Remove multiples of a given number from the list.

        Args:
        - nums: The list of numbers.
        - num: The number whose multiples should be removed.
        """
        for i in range(num, len(nums), num):
            nums[i] = -1

    def play_round(nums):
        """
        Play a round of the game.

        Args:
        - nums: The list of numbers for the current round.

        Returns:
        - True if a move was made, False otherwise.
        """
        primes = get_primes_up_to_n(max(nums))
        for prime in primes:
            if can_remove_number(nums, prime):
                remove_multiples(nums, prime)
                return True
        return False

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        nums_list = list(range(1, n + 1))
        round_number = 0

        while play_round(nums_list):
            round_number += 1

        if round_number % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
