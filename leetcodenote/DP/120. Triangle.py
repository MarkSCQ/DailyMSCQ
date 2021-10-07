"""
https://leetcode.com/problems/triangle/

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10

"""


import math


class Solution:
    def minimumTotal(self, triangle):

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    # ! head
                    triangle[i][j] = triangle[i-1][0] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    # ! tail
                    triangle[i][j] = triangle[i-1][-1] + triangle[i][j]
                else:
                    # ! middle contents
                    triangle[i][j] = triangle[i][j] + \
                        min(triangle[i-1][j-1], triangle[i-1][j])

        return min(triangle[-1])


"""
Official Solution

Algorithm:
Putting everything together, we get the following algorithm.

    Iterate through each row index between 1 and n - 1 inclusive (where n is the number of rows in triangle):
        Iterate through each col index between 0 and row inclusive:
            Initialize a variable smallestAbove to positive infinity:
                If col > 0:
                    Set smallestAbove to triangle[row - 1][col - 1].
                If col < row:
                    Set smallestAbove to be the min out of itself and triangle[row - 1][col].
            Set triangle[row][col] to be itself plus smallestAbove. Return the minimum value in triangle[n - 1].

"""


class Solution:
    def minimumTotal(self, triangle):
        for row in range(1, len(triangle)):
            for col in range(row + 1):
                smallest_above = math.inf
                if col > 0:
                    smallest_above = triangle[row - 1][col - 1]
                if col < row:
                    smallest_above = min(
                        smallest_above, triangle[row - 1][col])
                triangle[row][col] += smallest_above
        return min(triangle[-1])
