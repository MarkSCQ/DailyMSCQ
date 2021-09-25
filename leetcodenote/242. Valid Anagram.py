"""
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

# ! Solution 1 hashtable


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        for i in list(s):
            if i not in sd:
                sd[i] = 1
            else:
                sd[i] += 1
        for i in list(t):
            if i not in td:
                td[i] = 1
            else:
                td[i] += 1
        return True if sd == td else False

# ! Solution 2 Sorting


class Solution:
    def isAnagram(self, s, t):
        # sd = sorted(list(s))
        # td = sorted(list(t))

        # return True if sd==td else False
        return sorted(s) == sorted(t)
