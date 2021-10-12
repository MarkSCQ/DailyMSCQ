"""
https://leetcode.com/problems/surrounded-regions/

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.


Example 1:


Input: 
board = [["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]]

Output: [["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]]

Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:
Input: board = [["X"]]
Output: [["X"]]

"""


"""
Solution
1. Find all connected components of "O"s tant has at least one "O" taht is on the border, keep them as is

2. Flip all other "O"s to "X"

start from only border cells
"""


class Solution:
    def solve(self, board):

        height = len(board)
        width = len(board[0])

        # ! 2. searching
        def dfs(row, col):

            if row < 0 or row >= height or col < 0 or col >= width or board[row][col] != "O":
                return
            board[row][col] = "G"

            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        # ! 1. perform searching
        for i in range(height):
            dfs(i, 0)
            dfs(i, width-1)

        for j in range(width):
            dfs(0, j)
            dfs(height-1, j)

        dic = {"G": "O", "X": "X", "O": "X"}

        # ! 3. recover
        for row in range(height):
            for col in range(width):
                board[row][col] = dic[board[row][col]]

        return board


"""
BFS Version

Starting from border. Using deque as queue

"""


class Solution2:
    def solve(self, board):

        height = len(board)
        width = len(board[0])
        dires = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        from collections import deque

        # ! step 2
        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            while queue:
                r, c = queue.popleft()
                if board[r][c] != "O":
                    continue
                board[r][c] = "G"
                for i in range(len(dires)):
                    nrow = r + dires[i][0]
                    ncol = c + dires[i][1]
                    if nrow < 0 or nrow >= height or ncol < 0 or ncol >= width:
                        continue
                    queue.append((nrow, ncol))

        # ! step 1 perform search
        for i in range(height):
            bfs(i, 0)
            bfs(i, width-1)

        for j in range(width):
            bfs(0, j)
            bfs(height-1, j)

        dic = {"G": "O", "X": "X", "O": "X"}

        # ! step 3 revover
        for row in range(height):
            for col in range(width):
                board[row][col] = dic[board[row][col]]

        return board
