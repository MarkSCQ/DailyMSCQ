"""
https://leetcode.com/problems/minesweeper/

Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.


Example 1:
Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

Example 2:
Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

"""


"""
Click, the position we click to start.
1. check if the click(current) cell is bomb
2. count the bombs around the click(current) cell
3. if the number of bombs is greater than 0, update the digits of click(current) cell
4. if current cell is not bomb, there is not bomb arond the current cell,
    then making dfs to update the board recursively

"""


class solution:
    def updateBoard(self, board, click):
        # ! directions
        dire = [(1, 0), (-1, 0), (0, 1), (0, -1),
                (1, 1), (1, -1), (-1, 1), (-1, -1)]
        crow, ccol = click
        height = len(board)
        width = len(board[0])
        mines = 0
        # ! change M if the clicked cell is bomb
        if board[crow][ccol] == "M" or board[crow][ccol] == "X":
            board[crow][ccol] = "X"
            return board

        # ! count the bombs around
        for d in dire:
            nrow = crow+d[0]
            ncol = ccol+d[1]

            if nrow < 0 or nrow >= height or ncol < 0 or ncol >= width:
                continue
            if board[nrow][ncol] == "M":
                mines += 1

        # ! update digists if the amount of around mines is greater than 0
        if mines > 0:
            board[crow][ccol] = str(mines)
            return board

        # ! if there is no bomb around, set the current cell as blank
        board[crow][ccol] = 'B'

        # ! doing dfs recursively
        for d in dire:
            nrow = crow+d[0]
            ncol = ccol+d[1]
            if nrow < 0 or nrow >= height or ncol < 0 or ncol >= width:
                continue
            if board[nrow][ncol] == "E":
                self.updateBoard(board, [nrow, ncol])

        return board


"""
BFS
"""


class Solution:
    def updateBoard(self, board, click):

        dire = [(1, 0), (-1, 0), (0, 1), (0, -1),
                (1, 1), (1, -1), (-1, 1), (-1, -1)]
        crow, ccol = click
        height = len(board)
        width = len(board[0])

        from collections import deque

        def bfs(row, col, board):
            queue = deque()
            queue.append((row, col))
            visited = [[0 for i in range(width)] for j in range(height)]

            while queue:
                r, c = queue.popleft()
                count = 0

                for i in range(len(dire)):
                    nrow = r+dire[i][0]
                    ncol = c+dire[i][1]
                    if nrow < 0 or nrow >= height or ncol < 0 or ncol >= width:
                        continue
                    if board[nrow][ncol] == "M":
                        count += 1

                if count > 0:
                    board[r][c] = str(count)
                else:
                    board[r][c] = 'B'
                    for i in range(len(dire)):
                        nrow = r+dire[i][0]
                        ncol = c+dire[i][1]
                        if nrow < 0 or nrow >= height or ncol < 0 or ncol >= width:
                            continue
                        if board[nrow][ncol] == "E" and visited[nrow][ncol] == 0:
                            queue.append((nrow, ncol))
                            visited[nrow][ncol] = 1

        if board[crow][ccol] == "M":
            board[crow][ccol] = "X"
        else:
            bfs(crow, ccol, board)

        return board
