#!/usr/bin/python3
"""Prime Game."""


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_next_prime(nums):
        for num in nums:
            if is_prime(num):
                return num
        return None

    def remove_multiples(nums, prime):
        return [num for num in nums if num % prime != 0]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        current_player = 'Maria'
        game_nums = list(range(1, n + 1))

        while True:
            prime = find_next_prime(game_nums)

            if prime is None:
                break  # No prime numbers left

            game_nums = remove_multiples(game_nums, prime)

            if not game_nums:
                if current_player == 'Maria':
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            current_player = 'Ben' if current_player == 'Maria' else 'Maria'

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
