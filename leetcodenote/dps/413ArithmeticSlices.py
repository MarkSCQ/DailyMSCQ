"""
https://leetcode.com/problems/arithmetic-slices/
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

Example 2:
Input: nums = [1]
Output: 0

"""


class Solution:
    def numberOfArithmeticSlices(self, nums):
        # ! initialize helper
        # ! in helper, each cell denotes the valid slices from beginning of the array to current element 
        helper = [0 for i in range(len(nums))]

        for i in range(2, len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                helper[i] = helper[i-1]+1
        # ! each cell represents the valid slices from head to its element,
        # ! sum them up will have the total amount
        return sum(helper)
