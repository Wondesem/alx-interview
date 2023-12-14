#!/usr/bin/python3
"""
method to determine the number of occurance of a letter
"""
"""
it returns an integer if n is impossible returns 0
"""

def minOperations(n):
    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
