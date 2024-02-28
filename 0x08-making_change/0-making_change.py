#!/usr/bin/python3
"""Determine the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins.sort(reverse=True)

    num_coins = 0
    i = 0

    while total > 0 and i < len(coins):
        if coins[i] <= total:
            # Use as many coins of the largest denomination as possible
            num_coins += total // coins[i]
            total %= coins[i]
        i += 1

    return num_coins if total == 0 else -1
