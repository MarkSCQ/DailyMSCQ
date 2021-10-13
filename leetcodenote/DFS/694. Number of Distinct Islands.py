"""
https://leetcode.com/problems/number-of-distinct-islands/

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Return the number of distinct islands.


Example 1:
Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Output: 1

Example 2:
Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
Output: 3

"""


"""
The distinct islands, definition: different shape. position of the islands is not an issue

The seenIslands, the cell used is put in this set, can be understood as marked or visited.


"""


class Solution:
    def numDistinctIslands(self, grid):

        seenIslands = set()
        res = set()

        height = len(grid)
        width = len(grid[0])

        def dfs(row, col):
            # ! boundary check
            if row < 0 or col < 0 or row >= height or col >= width:
                return
            # ! in marked position or is not land
            if (row, col) in seenIslands or grid[row][col] == 0:
                return

            # ! add to seen
            seenIslands.add((row, col))
            # ! the shape of curr cell,
            # ! 0 0 0 1
            # ! 0 0 1 1
            # ! 0 0 0 1
            # ! position of the islands can be calculated as below
            # ! original row = 0, original column = 3
            # !      (0,3)             (0,0)
            # ! (1,2)(1,3)  =>   (1,-1)(1,0)
            # !      (2,3)             (2,0)

            curr.add((row-orirow, col-oricol))

            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for row in range(height):
            for col in range(width):
                orirow = row
                oricol = col
                curr = set()
                dfs(row, col)
                if curr:
                    res.add(frozenset(curr))

        return len(res)
