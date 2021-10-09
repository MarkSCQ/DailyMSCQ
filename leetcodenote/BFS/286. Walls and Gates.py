"""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.


Example 1:
Input: rooms = 
[
    [inf,  -1,   0,    inf],
    [inf,  inf,  inf,   -1],
    [inf,  -1,   inf,   -1],
    [0,    -1,   inf,  inf]
]

Output: 
[
    [3,  -1,  0,   1],
    [2,   2,  1,  -1],
    [1,  -1,  2,  -1],
    [0,  -1,  3,   4]
]

Example 2:
Input: rooms = [[-1]]
Output: [[-1]]

Example 3:
Input: rooms = [[2147483647]]
Output: [[2147483647]]

Example 4:
Input: rooms = [[0]]
Output: [[0]]
"""


class Solution:
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        height = len(rooms)
        width = len(rooms[0])
        inf = 2147483647
        if height == 0:
            return [[-1]]

        dire = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        from collections import deque

        queue = deque()

        for i in range(height):
            for j in range(width):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:

            row, col = queue.popleft()
            for i in range(len(dire)):
                nrow = row + dire[i][0]
                ncol = col + dire[i][1]
                if nrow < 0 or ncol < 0 or nrow >= height or ncol >= width or rooms[nrow][ncol] != inf:
                    continue
                rooms[nrow][ncol] = rooms[row][col]+1
                queue.append((nrow, ncol))

        return rooms
