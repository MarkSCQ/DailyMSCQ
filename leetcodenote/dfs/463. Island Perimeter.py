"""
https://leetcode.com/problems/island-perimeter/

NOT DFS BUT SIMILAR TO OTHER ISLAND QUESTIONS

"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        result = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    if i == 0:
                        up = 0
                    else:
                        up = grid[i - 1][j]

                    if j == 0:
                        left = 0
                    else:
                        left = grid[i][j - 1]

                    if i == height - 1:
                        down = 0
                    else:
                        down = grid[i + 1][j]

                    if j == width - 1:
                        right = 0
                    else:
                        right = grid[i][j + 1]
                    result += (4 - (up + down + right + left))
        return result