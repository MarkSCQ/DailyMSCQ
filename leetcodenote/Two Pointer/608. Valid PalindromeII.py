"""
https://leetcode.com/problems/valid-palindrome-ii/

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

"""

"""

Idea: Two pointers. 
starting from head and tail, each time we check whether there exists mismatching for substring.

if head and tail matches(head and tail index increase and decrese at the same time), then we can say 0-head and tail-len(string)-1 is palindrome

If mismatching exists, then we need to check   
        -> what if we exclude the tail element s[head:tail], will this make substring palindrome? (delete the tail element)
        -> what if we exclude the head element s[head+1:tail+1], will this make substring palindrome? (delete the head element)
Thess two check is "at most deleteing one character"

"""


class Solution:
    def validPalindrome(self, s):
        head = 0
        tail = len(s)-1

        while head < tail:

            if s[head] != s[tail]:
                leftsub = s[head:tail]
                rightsub = s[head+1:tail+1]
                return leftsub == leftsub[::-1] or rightsub == rightsub[::-1]
            head += 1
            tail -= 1
        return True
