#!/usr/bin/python3
"""perimeter module
"""


def island_perimeter(grid):
    """returns the perimeter of an island
       @grid: list of array of integers 0 and 1
    """
    if len(grid) < 3:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # perimeter of a single cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
