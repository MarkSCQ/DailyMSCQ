"""
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""


class Solution:
    def lengthOfLIS(self, nums):
        # ! initialize hepler array, using 1 to denote that at least exist one subsequence, number itself
        helper = [1 for i in range(len(nums))]
        # ! outer interation, scan the whole array
        for i in range(len(nums)):
            # ! inner iteration, each time, only consider the elements before the current number.
            for j in range(i):
                if nums[i] > nums[j]:
                    # ! scan the sub array, if nums[i]>nums[j] then we can update the value.
                    # ! this update is based on the previous values.
                    helper[i] = max(helper[i], helper[j]+1)
        return max(helper)
