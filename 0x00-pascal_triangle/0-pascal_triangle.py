#!/usr/bin/python3

"""Create a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer """

def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    res = list()
    if n <= 0:
        return res
    else:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
