"""
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

Given a string s, return the length of the longest substring that contains at most two distinct characters.

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        # ! when the size of string is smaller than 3, which means there at most 2 characters
        # ! just aa/ab all meet requirements, at most 2 characters
        if len(s) < 3:
            return len(s)

        # ! charset,
        # ! store relationship element-most latest occurance index
        charset = {}
        left = 0
        right = 0
        # ! set as 2 because we have pass the special case when length is smaller than 3
        res = 2
        # ! window shifts to right
        while right < len(s):
            # ! no matter what we have in this right, we will put it into the dic
            # ! the relationship is the element-latest occurance
            # ! adapt the current element to the dict
            charset[s[right]] = right
            right += 1
            # ! check whether the newly added element createss invalidation
            if len(charset) == 3:
                # ! we use dict to store the element-most latest occurance index 
                # ! use this relationship to get the leftmost element
                deleteIndex = min(charset.values())
                # ! remove the element
                del charset[s[deleteIndex]]
                # ! left shifts to right
                left = deleteIndex+1
            res = max(res, right-left)
        return res
