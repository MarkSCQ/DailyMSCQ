"""
https://leetcode.com/problems/word-search/

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
        # ! path set store records
        pathrecord = set()


        def dfs(r, c, i):
            if i == len(word):
                return True
            # ! boundary check and word check
            if r < 0 or c < 0 or r >= height or c >= width or (r, c) in pathrecord or board[r][c] != word[i]:
                return False
            
            pathrecord.add((r, c))
            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1)
                   or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))

            pathrecord.remove((r, c))
            return res

        # ! apply dfs on each cell
        for i in range(height):
            for j in range(width):
                if dfs(i, j, 0):
                    return True
        return False
