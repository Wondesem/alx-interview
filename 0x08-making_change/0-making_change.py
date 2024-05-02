#!/usr/bin/python3

"""This is an app that convert the coin in to total"""


def makeChange(coins, total):
    """The function returns fewest number of coins needed to meet total"""

    if total <= 0:
        return 0
    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
                if total == 0:
                    return counter

    return -1
