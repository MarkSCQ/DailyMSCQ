"""
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.


Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

"""

"""
each cell has its own value, we need to get the minimum path, direction: right and down.

we use one helper matrix  ini-matrix to help solve this question.

discuss this question with four different situations.
1. when i==0 and j==0, it means we are at the start point, assign the value to matrix[0][0]
2. when i==0, it means we are at row 0. We can only accept the values from our left. 
3. when j==0, this means we are on the left edge, there is one way we can get previous value from -- top.
4. when j!=0 and i!=0, the aim of this question is going to get the minimum path value, then we accept the minimum of left and top value.
5. finally return the rightmost-bottom value as our result

"""

class Solution:
    def minPathSum(self, grid):

        ini_matrix = [[0 for j in range(len(grid[0]))]
                      for i in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    ini_matrix[0][0] = grid[0][0]
                elif i == 0:
                    ini_matrix[i][j] = ini_matrix[i][j-1]+grid[i][j]
                elif j == 0:
                    ini_matrix[i][j] = ini_matrix[i-1][j]+grid[i][j]
                else:
                    ini_matrix[i][j] = min(
                        ini_matrix[i-1][j], ini_matrix[i][j-1])+grid[i][j]
        return ini_matrix[-1][-1]
