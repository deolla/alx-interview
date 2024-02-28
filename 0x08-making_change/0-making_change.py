#!/usr/bin/python3
"""Determine the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    # Iterate through each coin denomination
    for coin in coins:
        # Update dp array for each amount starting from coin value
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
