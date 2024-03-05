#!/usr/bin/python3
"""Create a function that returns the perimeter of a island."""


def island_perimeter(grid):
    """Return the perimeter of the island."""
    perimeter = 0

    # Iterate over each row in the grid
    for m in range(len(grid)):
        # Iterate over each cell in the row
        for j in range(len(grid[m])):
            # Check if the cell is land
            if grid[m][j] == 1:
                perimeter += 4  # Increment the perimeter by 4

                # Check the neighboring cells
                if m > 0 and grid[m-1][j] == 1:  # Check cell above
                    perimeter -= 1
                if m < len(grid) - 1 and grid[m+1][j] == 1:  # Check cell below
                    perimeter -= 1
                if j > 0 and grid[m][j-1] == 1:  # Check cell to the left
                    perimeter -= 1
                if j < len(grid[m]) - 1 and grid[m][j+1] == 1:
                    perimeter -= 1

    return perimeter
