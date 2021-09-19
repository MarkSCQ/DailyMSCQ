"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
class Solution:
    def longestCommonPrefix(self, strs):
        # ! special cases 
        # ! if the input string list is empty 
        # ! or the input string list only have one string
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        # ! initialize prefix count
        prefix = strs[0]
        i = 0
        for st in strs:
            # ! i is used in string prefix comparison
            i = 0
            # ! update the maximum prefix length in each round, 
            # ! this is set as a boundary, not the final result
            # ! by comparing with current string in string list
            lenstr = len(st) if len(st) < len(prefix) else len(prefix)
            # ! compare and get the maximum length, i is used for counting length
            while i < lenstr:
                if st[i] == prefix[i]:
                    i += 1
                else:
                    break
            # ! set the prefix, starting from start to index i. 
            # ! Notice, this will not include the element in index i. 
            # ! The elements of prefix is from 0 to i-1 of string st 
            prefix = st[:i]
        return prefix
