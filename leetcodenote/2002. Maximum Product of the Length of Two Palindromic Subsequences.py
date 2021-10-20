"""
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

Given a string s, find two disjoint palindromic subsequences of s such that the product of their lengths is maximized. The two subsequences are disjoint if they do not both pick a character at the same index.

Return the maximum possible product of the lengths of the two palindromic subsequences.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters. A string is palindromic if it reads the same forward and backward.

Example 1:
example-1
Input: s = "leetcodecom"
Output: 9
Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
The product of their lengths is: 3 * 3 = 9.

Example 2:
Input: s = "bb"
Output: 1
Explanation: An optimal solution is to choose "b" (the first character) for the 1st subsequence and "b" (the second character) for the 2nd subsequence.
The product of their lengths is: 1 * 1 = 1.

Example 3:
Input: s = "accbcaxxcxx"
Output: 25
Explanation: An optimal solution is to choose "accca" for the 1st subsequence and "xxcxx" for the 2nd subsequence.
The product of their lengths is: 5 * 5 = 25.
"""


"""
check two string or two list is disjoint - using bitmask

example 3
    origin  leetcodecom
    code    00000000000
    ete     01010001000
    cdc     00001010100
using &     00000000000
"""


class Solution:
    def maxProduct(self, s):
        strlen = len(s)
        dic = {}

        # ! 1<<N == 2**N
        # ! using bit mask to searching for the potential solution, 
        # ! NOTE: these potential solutions may not be the palidromic sequence
        for mask in range(1, 1 << strlen):
            subseq = ""
            for i in range(strlen):
                # ! searching from 0 to i, substring
                if mask & 1 << i:
                    # ! disjoint cases condition
                    subseq += s[strlen-1-i]
            # ! if palindromic
            if subseq == subseq[::-1]:
                dic[mask] = len(subseq)
        res = 0
        for key1 in dic:
            for key2 in dic:
                if key1 & key2 == 0:
                    res = max(res, dic[key1]*dic[key2])
        return res
