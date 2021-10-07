"""
https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""

"""
BFS
Notice: the cell has three states. 2 1 and 0. 
Initialization:
    The rotted, adding into queue.
    The fresh, count the amount 
    Initilize time, minu=0

In BFS search, not only finish/simulate the rotting procedures, but also count the minutes to accomplish the procedure.

"""


class Solution:
    def orangesRotting(self, grid):
        height = len(grid)
        width = len(grid[0])

        from collections import deque

        rotted = deque()
        fresh = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 2:
                    rotted.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minu = 0
        while len(rotted) > 0:
            # ! count the current amount of rotted oranges and process this amount of oranges
            size = len(rotted)
            for k in range(size):
                row, col = rotted.popleft()
                for i in range(len(dirs)):
                    nrow = row+dirs[i][0]
                    ncol = col+dirs[i][1]

                    if nrow < 0 or ncol < 0 or nrow >= height or ncol >= width or grid[nrow][ncol] == 2 or grid[nrow][ncol] == 0:
                        continue
                    grid[nrow][ncol] = 2
                    fresh -= 1
                    rotted.append((nrow, ncol))
            # ! after the procedure minutes+1
            minu += 1

        return minu-1 if fresh == 0 else -1
