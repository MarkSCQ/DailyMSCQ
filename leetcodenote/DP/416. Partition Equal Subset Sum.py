"""
https://leetcode.com/problems/partition-equal-subset-sum/
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

"""


class Solution:
    def canPartition(self, nums):
        sm = sum(nums)

        if sm % 2 != 0:
            return False

        helper = [0 for i in range(sm+2)]

        helper[0] = 1

        for num in nums:
            for i in range(sm+1, -1, -1):
                if helper[i]:
                    helper[i+num] = 1
                if helper[sm//2]:
                    return True
        return False
