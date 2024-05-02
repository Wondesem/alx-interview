#!/usr/bin/python3


"""This app changes coin into amount"""


def makeChange(coins, total):

    """Return: fewest number of coins needed to meet total"""
    if total <= 0:
        return 0
    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for( i in coin):
            while(total >= i):
                counter += 1
                total -= i
                if(coin == 0):
                    return counter


        return -1
