"""
https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

325. Maximum Size Subarray Sum Equals k
Medium

Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:
Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

Example 2:
Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
"""


class Solution:
    def maxSubArrayLen(self, nums, k):
        # ! initialize current sum and current longest 
        currsum = 0
        currlongest = 0
        # ! using dictionary to store the sum:index pair. the sum here is the accumulative sum.
        # ! in sumindex dictionary
        # ! the value of each pair, it denotes that the accumulative sum calculation stops at this value. 
        # ! the key of each pair is accumulative sum value
        sumindex = {}
        for i in range(len(nums)):
            currsum += nums[i]
            # ! if the accumulative sum happens to equal to K then assign the current longest with max(i+1,current longest length)
            if currsum == k:
                currlongest=max(currlongest,i+1)

            # ! if current sum - k is in the accumulative sum dictionary
            if currsum-k in sumindex:
                # ! assign the current longest with the max of current longest value and i-sumindex[currsum-k] which is the length from num[i] to (currsum-k) 
                currlongest = max(currlongest, i-sumindex[currsum-k])

            # ! if current sum is not in data dictionary, then add curernt sum and index dictionary
            if currsum not in sumindex:
                sumindex[currsum] = i

        return currlongest
