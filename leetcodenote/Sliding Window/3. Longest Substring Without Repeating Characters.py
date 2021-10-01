'''
Given a string s, find the length of the longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        # ! character dictionary
        dic = {}
        # ! results length of longest substring
        res = 0
        # ! sliding window, left index, used to contrast the sliding window
        left = 0
        # ! sliding window, right index, used to extend the sliding window
        right = 0
        # ! when right is smaller than the length of string s.
        # ! the maximum length that satisfiied the description is len of original string
        while right < len(s):
            # ! set the right window element
            r = s[right]
            # ! check the right index element
            if r not in dic:
                dic[r] = 1
            else:
                dic[r] += 1
            # ! if duplicated then shift the left of window to right
            # ! be careful, the while below will be triggered when dir[r]>1
            while dic[r] > 1:
                # ! get left index element
                # ! notice the left here is the duplicate element 
                l = s[left]
                # ! left element amount -1
                dic[l] -= 1
                # ! shift the left edge of window to right
                left += 1
            # ~ comparing the previous max length and current max length
            res = max(res, right-left+1)
            # ~ right index extend, shift right index to tail, +1
            right += 1
        return res
