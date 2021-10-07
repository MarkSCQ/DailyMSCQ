"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


Example 1:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], 
        word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], 
        word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]],
        word = "ABCB"
Output: false

"""


class Solution:
    def exist(self, board, word):

        height = len(board)
        width = len(board[0])
        # ! path records
        pathrecord = set()

        # ! searching word,
        # ! r -> row index
        # ! c -> col index
        # ! i -> index in word
        def dfs(r, c, i):
            if i == len(word):
                return True
            # ! out of boundary check, repeated path check, word check
            if r < 0 or c < 0 or r >= height or c >= width  \
                    or (r, c) in pathrecord  \
                    or board[r][c] != word[i]:
                return False
            # ! add path to records
            pathrecord.add((r, c))
            # ! recursion, move to four directions and get results
            res = (
                dfs(r+1, c, i+1) or
                dfs(r-1, c, i+1) or
                dfs(r, c+1, i+1) or
                dfs(r, c-1, i+1)
            )
            # ! remove position records (recover in backtrack)
            pathrecord.remove((r, c))
            return res

        for i in range(height):
            for j in range(width):
                # ! return true if we can find the word at current postiion i,j
                # ! return False we cannot find the word at current position i,j
                if dfs(i, j, 0):
                    return True
        return False
