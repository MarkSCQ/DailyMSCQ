"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

"""


class Solution:
    def repeatedSubstringPattern(self, s):
        # ! s2 is s append with s, and remove the first and the last elements
        s2 = (s+s)[1:-1]
        # ! lets take a look at s2; How we make the s2? basically using two s;
        # ! if s is constructed by its substring, for example, s is make by string1+string1
        # ! when two s is connected together, we will find the connected s is [string1+string1]+[string1+string1]
        # ! if we remove the first and last character element, then first string and last string will not be complete.
        # ! if the string is constructed by the same meta string, then the second string and third string is the original string. 
        return True if s in s2 else False
