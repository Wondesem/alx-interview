#!/usr/bin/python3

<<<<<<< HEAD

"""This app changes coin into amount"""


def makeChange(coins, total):

    """Return: fewest number of coins needed to meet total"""
=======
"""This is an app that convert the coin in to total"""


def makeChange(coins, total):
    """The function returns fewest number of coins needed to meet total"""

>>>>>>> 75d02383d8a5ec7e81e3b87cf4e6b8cc2a38002d
    if total <= 0:
        return 0
    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
<<<<<<< HEAD
        for( i in coin):
            while(total >= i):
                counter += 1
                total -= i
                if(coin == 0):
                    return counter


        return -1
=======
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
                if total == 0:
                    return counter

    return -1
>>>>>>> 75d02383d8a5ec7e81e3b87cf4e6b8cc2a38002d
