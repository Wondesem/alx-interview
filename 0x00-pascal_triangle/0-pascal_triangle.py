#!/usr/bin/python3

"""Create a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer """

def pascal_triangle(n):
    """returns empty list if n <= 0"""
    my_list = []
    if n <= 0:
        return my_list
    for i in range(n):
        first_row = [1]
        if my_list:
            last_row = my_list[-1]
            first_row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            first_row.append(1)
        my_list.append(first_row)
    return (my_list)
