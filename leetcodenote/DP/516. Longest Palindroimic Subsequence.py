"""
https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

"""


"""
! Solution Analysis

    dp[i][j] := solution of s[i..j]
    stage: length of the substring

    for len=1 to n:
        for i=0 to n-len:
            j=i+len-1
            if s[i]==s[j]:
                dp[i][j] = dp[i+1][j-1]+2
            else:
                dp[i][j] = max(dp[i+1][j],dp[i][j-1])
    return dp[0][n-1]

! Case Analysis

base case:
    a->dp[i][j] = 1

case 1: s[i]==s[j] 
        
        a******a -> dp[i][j] = dp[i+1][j-1]+2
                    dp[i][j] is the solution of string start i to j.
                    dp[i+1][j-1] is the ****** 
                    +2 is two a, the head one and tail one

case 2: s[i]!=s[j]

        ab******b -> dp[i][j] = dp[i+1][j]
        a******ab -> dp[i][j] = dp[i][j-1]
        ^       ^
        i       j

"""


class Solution:
    def longestPalindromeSubseq(self, s):

        ssize = len(s)
        if ssize == 1:
            return 1
        # ! initialize dp
        dp = [[0 for i in range(ssize)] for j in range(ssize)]

        # ! using i and j to denote the starting and ending index
        # ! dp[i][j] denotes the longest palindrome subsequence from character index i to character index j

        # ! outer for loop, the length of subsequence
        # ! inner for loop, the starting index
        for l in range(1, ssize+1):
            for i in range(ssize-l+1):
                # ! set ending index
                j = i+l-1
                # ! i==j base case, set as 1
                if j == i:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:
                    # ! case 1
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    # ! case 2
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][ssize-1]
