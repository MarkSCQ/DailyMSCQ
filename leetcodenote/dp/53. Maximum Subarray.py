"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

"""


"""
Solution 1 Kadane's algorithm 卡蛋算法

"""


class Solution:
    def maxSubArray(self, nums):
        currSubArrSum = nums[0]
        currMax = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            currSubArrSum = max(num, currSubArrSum+num)
            currMax = max(currMax, currSubArrSum)
        return currMax




"""
Divide and Conquer

split the array into left and rightgi

compare the combined left sum and right sum
"""
class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        def fs(nums,left,right):
            if left>right:
                return -float('inf')
            mid = left+(right-left)//2
            
            leftsum = 0
            rightsum = 0
            
            curr = 0
            for i in range(mid-1,left-1,-1):
                curr+=nums[i]
                leftsum=max(leftsum,curr)
            curr = 0
            for i in range(mid+1,right+1):
                curr+=nums[i]
                rightsum=max(rightsum,curr)
                
            combinedsum=nums[mid]+leftsum+rightsum
            lefthalf = fs(nums,left,mid-1)
            righthalf = fs(nums,mid+1,right)
            return max(combinedsum,lefthalf,righthalf)
        return fs(nums,0,len(nums)-1)