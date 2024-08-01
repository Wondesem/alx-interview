#!/usr/bin/python3
"""
This function calculates the perimeter of island described in grid
"""


def island_perimeter(grid):
    """
    returns grid sides 0 as water and 1 as land.
    """

    visited = set()

    def dfs(i, j):
        '''dfs implementation'''
        if i >= len(grid) or j >= len(grid[0]) or \
                i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0

        visited.add((i, j))
        perimeter = dfs(i, j + 1)
        perimeter += dfs(i + 1, j)
        perimeter += dfs(i, j - 1)
        perimeter += dfs(i - 1, j)
        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)
