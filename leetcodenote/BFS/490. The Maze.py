"""
https://leetcode.com/problems/the-maze/

There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination, otherwise return false.

You may assume that the borders of the maze are all walls (see examples).


Example 1:
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.


Example 2:
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination but you cannot stop there.


Example 3:
Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: false


"""



"""
Starting from start to find whehter we can stop as destination. 
Notice, the question mentioned that it wont stop until hitting a wall.

As shown in the example below, the start is our destination
We cannot stop at the star, since we cannot hit the wall when reaching the start

---------------------  |   -------------------------
|                   |  V  |                       | 
|                   |     |                       |
|                   |  *  |                       |
|                   |     |                       |
---------------------     -------------------------
|                                                 |
---------------------------------------------------

"""


class Solution:
    def hasPath(self, maze, start, destination):
        from collections import deque

        height = len(maze)
        width = len(maze[0])
        queue = deque()
        queue.append((start[0], start[1]))
        dires = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        marked = [[False for i in range(width)] for j in range(height)]

        while queue:

            currx, curry = queue.popleft()
            if currx == destination[0] and curry == destination[1]:
                return True
            marked[currx][curry] = True

            for i in range(len(dires)):
                newx = currx+dires[i][0]
                newy = curry+dires[i][1]

                while newx >= 0 and newy >= 0 and newx < height and newy < width and maze[newx][newy] == 0:
                    newx += dires[i][0]
                    newy += dires[i][1]

                if not marked[newx-dires[i][0]][newy-dires[i][1]]:
                    queue.append((newx-dires[i][0], newy-dires[i][1]))
                    marked[newx-dires[i][0]][newy-dires[i][1]] = True

        return False
