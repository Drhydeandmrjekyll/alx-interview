#!/usr/bin/python3
"""
Module for making change problem
"""


def makeChange(coins, total):
    """
    Determines fewest number of coins needed to meet given amount total
    Args:
        coins (list): A list of values of  coins in your possession
        total (int): The target amount total
    Returns:
        int: Fewest number of coins needed to meet total
    """
    memo = {}

    def dp(total):
        if total < 0:
            return float('inf')
        if total == 0:
            return 0
        if total in memo:
            return memo[total]

        min_coins = float('inf')
        for coin in coins:
            min_coins = min(min_coins, dp(total - coin) + 1)

        memo[total] = min_coins
        return min_coins

    result = dp(total)
    return result if result != float('inf') else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
