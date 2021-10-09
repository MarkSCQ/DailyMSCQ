"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:


Input: board = [
                ["o","a","a","n"],
                ["e","t","a","e"],
                ["i","h","k","r"],
                ["i","f","l","v"]
                ], 
        words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

"""

"""
! DFS(Backtracking) + trie tree structure

! Three steps
! 1. constructing dfs searching
! 2. make prefix
! 3. apply dfs recursively

"""


class Solution:
    def findWords(board, words):
        ans = []
        # ! construct prefix structure
        prefix = {}
        for word in words:
            node = prefix
            for i in word:
                node = node.setdefault(i, {})
            # ! using # to hold the word
            node["#"] = word
        height = len(board)
        width = len(board[0])
        dires = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # ! dfs
        def DFSSearching(row, col, parent):
            currLetter = board[row][col]
            prefixNode = parent[currLetter]
            matchword = prefixNode.pop("#", False)
            # ! if word matches add to the results
            if matchword:
                ans.append(matchword)
            # ! mark the used elements
            board[row][col] = "$"

            for i in range(len(dires)):
                nrow = row + dires[i][0]
                ncol = col + dires[i][1]
                # ! boundary check
                if nrow < 0 or nrow >= height or ncol < 0 or ncol >= width:
                    continue
                # ! if one is in prefixNode check
                if not board[nrow][ncol] in prefixNode:
                    continue
                DFSSearching(nrow, ncol, prefixNode)
            # ! recover to previous state after finishing one search
            print("Finished ", currLetter)
            board[row][col] = currLetter

            # ! remove useless nodes
            if not prefixNode:
                parent.pop(currLetter)

        for row in range(height):
            for col in range(width):
                if board[row][col] in prefix:
                    DFSSearching(row, col, prefix)
        return ans


def findWords(board, words):
    ans = []
    # ! construct prefix structure
    prefix = {}
    for word in words:
        node = prefix
        for i in word:
            node = node.setdefault(i, {})
        # ! using # to hold the word
        node["#"] = word
    height = len(board)
    width = len(board[0])
    dires = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # ! dfs
    def DFSSearching(row, col, parent):
        currLetter = board[row][col]
        prefixNode = parent[currLetter]
        matchword = prefixNode.pop("#", False)
        # ! if word matches add to the results
        if matchword:
            ans.append(matchword)
        # ! mark the used elements
        board[row][col] = "$"

        for i in range(len(dires)):
            nrow = row + dires[i][0]
            ncol = col + dires[i][1]
            # ! boundary check
            if nrow < 0 or nrow >= height or ncol < 0 or ncol >= width:
                continue
            # ! if one is in prefixNode check
            if not board[nrow][ncol] in prefixNode:
                continue
            DFSSearching(nrow, ncol, prefixNode)
        # ! recover to previous state after finishing one search
        board[row][col] = currLetter

        # ! remove useless nodes
        if not prefixNode:
            parent.pop(currLetter)

    for row in range(height):
        for col in range(width):
            if board[row][col] in prefix:
                DFSSearching(row, col, prefix)
    return ans


board = [
    ["o", "a", "a", "n"], ["e", "t", "a", "e"],
    ["i", "h", "k", "r"], ["i", "f", "l", "v"]
]
words = ["oath", "pea", "eat", "rain"]


findWords(board, words)
