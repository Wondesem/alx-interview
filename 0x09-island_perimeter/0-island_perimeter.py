#!/usr/bin/python3
"""
This function calculates the perimeter of island described in grid
"""


def island_perimeter(grid):
    """
    returns grid sides 0 as water and 1 as land.
    """

    perimeter = 0
    grid_length = len(grid)
    for row in range(grid_length):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                if row - 1 < 0 or grid[row - 1][column] == 0:
                    perimeter += 1
                if column - 1 < 0 or grid[row][column - 1] == 0:
                    perimeter += 1
                if column + 1 >= len(grid[row]) or grid[row][column + 1] == 0:
                    perimeter += 1
                if row + 1 >= grid_length or grid[row + 1][column] == 0:
                    perimeter += 1
    return perimeter