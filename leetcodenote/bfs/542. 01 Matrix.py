"""
https://leetcode.com/problems/01-matrix/

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


! BFS solution from LC official site
A better brute force: Looking over the entire matrix appears wasteful and hence, we can use Breadth First Search (BFS) to limit the search to the nearest 0 found for each 1. As soon as a 0 appears during the BFS, we know that the 0 is the closest, and hence, we move to the next 1.

Think again: But, in this approach, we will only be able to update the distance of one 1 using one BFS, which could in fact, result in slightly higher complexity than the brute force approach. But hey, this could be optimized if we start the BFS from 0s and thereby, updating the distances of all the 1s in the path.

Algorithm

-> For our BFS routine, we keep a queue, q to maintain the queue of cells to be examined next.
-> We start by adding all the cells with 0s to q.
-> Intially, distance for each 0 cell is 0 and distance for each 1 is INT_MAX, which is updated during the BFS.
-> Pop the cell from queue, and examine its neighbors. If the new calculated distance for neighbor {i,j} is smaller, we add {i,j} to q and update dist[i][j].

"""



from collections import deque


"""
! BFS solution can be considered as below:
! - Initialize the output matrix by setting each cell as infinity value   
! - Add the 0 cell into queue for searching
! - Each time we will check the neighbors(four up down left and right) of current cell
! - 
"""


def updateMatrix(mat):
    # ! initialize distance matrix by using queue
    height = len(mat)
    width = len(mat[0])
    if height == 0:
        return mat
    # ! initialize distance matrix using 'inf' values
    dist = [[float('inf') for i in range(width)] for j in range(height)]
    queue = deque()
    # ! push all 0 cell in to queue
    for i in range(height):
        for j in range(width): 
            if mat[i][j] == 0:
                dist[i][j] = 0
                queue.append([i, j])

    # ! four directions
    # !     down    up       left     right
    dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    
    # ! if the queue is not none
    while len(queue) != 0:
        # ! pop the one cell from queue
        head = queue.popleft()
        # ! searching the four neighbours of current cell
        for i in range(len(dir)):
            new_row = head[0]+dir[i][0]
            new_col = head[1]+dir[i][1]
            # ! boundary check
            if new_row >= 0 and new_col >= 0 and new_row < height and new_col < width:
                # ! if the new row and column data pass the coundary check and the cell data is bigger than the current data+1
                if dist[new_row][new_col] > dist[head[0]][head[1]]+1:
                    dist[new_row][new_col] = dist[head[0]][head[1]]+1
                    # ! any updated cell will be add into queue
                    queue.append([new_row, new_col])

    for i in dist:
        print(i)
    return dist

"""
! DP



"""




"""
Solution 2 Dynamic Programming:

Intuition

The distance of a cell from 0 can be calculated if we know the nearest distance for all the neighbors, in which case the distance is minimum distance of any neightbor + 1. And, instantly, the words come to mind Dynamic Programming (DP)!!
For each 1, the minimum path to 0 can be in any direction. So, we need to check all the 4 directions. In one iteration from top to bottom, we can check left and top directions, and we need another iteration from bottom to top to check for right and bottom direction.

"""

def updateMatrix_DP(mat):
    pass







test1 = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

test2 = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]


updateMatrix(test2)
