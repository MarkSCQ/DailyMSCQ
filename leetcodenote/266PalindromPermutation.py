"""
https://leetcode.com/problems/palindrome-permutation/

Given a string s, return true if a permutation of the string could form a palindrome.

Example 1:

Input: s = "code"
Output: false
Example 2:

Input: s = "aab"
Output: true
Example 3:

Input: s = "carerac"
Output: true
"""

"""
Solution very straightforward, just take a look at the odd case of the string
"""


class Solution:
    def canPermutePalindrome(self, s):
        sdata = {}
        for char in s:
            if char not in sdata:
                sdata[char] = 1
            else:
                sdata[char] += 1
        oddcal = 0
        for char in sdata:
            if sdata[char] % 2 == 1:
                oddcal += 1
        return True if oddcal <= 1 else False
