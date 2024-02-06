#!/usr/bin/python3

"""
The is list of integers where:
- 0 represents water
- 1 represents land
- each cell is square with a side length of 1
- cells are connected horizontally/vertically (not diagonally)
- grid is rectangle with width and height not exceeding 100
"""
def island_perimeter(grid):
    """A function that returns the perimeter of the island described in grid."""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
