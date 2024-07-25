#!/usr/bin/python3
"""
A program that makes coin changes
"""


def makeChange(coins, total):
    dp = [0] + [total + 1] * total
    for coin in coins:
        for x in range(coin, total):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
