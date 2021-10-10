"""
https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


"""

"""
Starting from center to two edge
"""


class Solution:
    def countSubstrings(self, s):

        ans = 0
        sl = len(s)
        s = list(s)

        def searchPa(l1, l2):
            ans = 0
            while l1 >= 0 and l2 < sl:

                if s[l1] == s[l2]:
                    ans += 1
                    l1 -= 1
                    l2 += 1
                else:
                    break
            return ans

        for i in range(0, len(s)):
            ans += searchPa(i-1, i)
            ans += searchPa(i, i)
        return ans
