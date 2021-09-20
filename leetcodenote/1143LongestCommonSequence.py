"""
https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""

def longestCommonSubsequence(self, text1, text2):
    # ! initialize matrix. add extra column and row to simplify the implementation.
    # ! the matrix cell value describes that at current row and col, 
    # ! the length of max common subsequence
    helper = [[0 for i in range(len(text2)+1)]
                for i in range(len(text1)+1)]

    # ! calculate answer matrix from the bottom 
    for row in reversed(range(len(text1))):
        for col in reversed(range(len(text2))):
            # ! current answer is based on the previous. 
            # ! if the current character is equal, then adding the diagnoal with 1
            # ! else get the maximum of string1 and string2 current cell value.
            if text1[row] == text2[col]:
                helper[row][col] = helper[row+1][col+1]+1
            else:
                helper[row][col] = max(
                    helper[row][col+1], helper[row+1][col])
    
    return helper[0][0]


# class Solution:
#     def longestCommonSubsequence(self, text1, text2):

#         # Make a grid of 0's with len(text2) + 1 columns
#         # and len(text1) + 1 rows.
#         dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

#         # Iterate up each column, starting from the last one.
#         for col in reversed(range(len(text2))):
#             for row in reversed(range(len(text1))):
#                 # If the corresponding characters for this cell are the same...
#                 if text2[col] == text1[row]:
#                     dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]
#                 # Otherwise they must be different...
#                 else:
#                     dp_grid[row][col] = max(
#                         dp_grid[row + 1][col], dp_grid[row][col + 1])

#         # The original problem's answer is in dp_grid[0][0]. Return it.
#         return dp_grid[0][0]
