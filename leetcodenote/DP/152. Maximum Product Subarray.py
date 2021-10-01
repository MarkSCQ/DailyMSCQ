"""
https://leetcode.com/problems/maximum-product-subarray/
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:333333

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""

"""
! There exists three different situations
!   1.1 positive * positive = positive
!   1.2 negative * negative = positive
!   2   positive * negative = negative
!   3   anynumber * 0
!   
!   considering three cases, each time we need to calculate the current max and current min
!   becase current min might be negative and cureent number in the list may be negative too.
!
"""


class Solution:
    def maxProduct(self, nums):
        # ! maximum so far
        maxSF = nums[0]
        # ! minimum so far
        minSF = nums[0]

        result = maxSF

        for i in range(1, len(nums)):
            # ! current element
            curr = nums[i]
            tmpmax = max(curr*maxSF, curr*minSF, curr)
            minSF = min(curr*maxSF, curr*minSF, curr)
            maxSF = tmpmax
            result = max(result, maxSF)

        return result
