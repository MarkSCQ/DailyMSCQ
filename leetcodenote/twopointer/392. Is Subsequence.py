"""
https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
"""

"""
Solution two pointer
"""


class Solution:
    def isSubsequence(self, s, t):
        left = 0
        right = 0

        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
                right += 1
            elif s[left] != t[right]:
                right += 1
        return left == len(s)


"""
Solution DP - Two dimensional matrix

~This question is the exactly the same as leectode 1143.Longest Common Subsequence 


"""


class Solution:
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True

        lrow = len(s)
        lcol = len(t)
        helper = [[0 for i in range(lcol+1)] for j in range(lrow+1)]

        for row in reversed(range(lrow)):
            for col in reversed(range(lcol)):

                if s[row] == t[col]:
                    helper[row][col] = helper[row+1][col+1]+1
                else:
                    helper[row][col] = max(
                        helper[row+1][col], helper[row][col+1])
                # ! the difference between this question and leetcode 1143
                if helper[row][col] == lrow:
                    return True

        return False
