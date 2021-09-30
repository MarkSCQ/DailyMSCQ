
"""

https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


class Solution(object):
    def reverseString(self, s):
        head = 0
        tail = len(s)-1
        
        while head<tail:
            s[head],s[tail]=s[tail],s[head]
            head+=1
            tail-=1
            
        return s