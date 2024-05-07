#!/usr/bin/python3
"""
The app that returns all grid with water 0 and land 1
"""


def island_perimeter(grid):
    """
    Finds the perimeter of island gridded
    Args:
        grid: 2 lists of integer with 0 (water) and 1 (land)
    Return: 
        the perimeter of the island
    """

    per = 0
    for i in range(len(grid)):
        for n in range(len(grid[i])):
            if(grid[i][n]==1):
                if(i <= 0 or grid[i - 1][n] == 0):
                    per += 1
                if(i >= len(grid) - 1 or grid[i + 1][n] == 0):
                    per += 1
                if(n <= 0 or grid[i][n - 1] == 0):
                    per += 1
                if(n >= len(grid[i]) -1 or grid[i][n + 1] == 0):
                    per += 1

    return per
