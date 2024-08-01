#!/usr/bin/python3
"""
This function calculates the perimeter of island described in grid
"""


def island_perimeter(grid):
    """
    returns grid sides 0 as water and 1 as land.
    """

    perim = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i <= 0 or grid[i-1][j] == 0):
                perim += 1
            if(i >= len(grid) - 1 or grid[i+1][j] == 0):
                perim += 1
            if (j >= len(grid[i]) - 1 or grid[i][j+1] == 0):
                perim += 1
    return perim
