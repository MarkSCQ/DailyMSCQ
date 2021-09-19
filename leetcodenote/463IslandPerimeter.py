"""
463IslandPerimeter
"""
class Solution:
    def islandPerimeter(self, grid):
        height = len(grid)
        width = len(grid[0])
        result = 0
        for i in range(height):
            for j in range(width):
                # ! if the current cell is land
                if grid[i][j] == 1:
                    # ! if current cell is on the 0th row
                    if i == 0:
                        up = 0
                    else:
                        # ! if current cell is not on the 0th cell, this menas it may have an upper border
                        up = grid[i - 1][j]
                    
                    # ! fi the current cell is on the 0th col
                    if j == 0:
                        left = 0
                    else:
                        # ! it may have a border on the 0th col
                        left = grid[i][j - 1]
                    
                    # ! for the last row
                    if i == height - 1:
                        down = 0
                    else:
                        down = grid[i + 1][j]

                    # ! for the last col
                    if j == width - 1:
                        right = 0
                    else:
                        right = grid[i][j + 1]
                    # ! add up all the calculations for the current cell
                    result += (4 - (up + down + right + left))
        return result
