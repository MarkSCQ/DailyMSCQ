"""

https://leetcode.com/problems/maximum-product-subarray/


Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.


Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""


"""

! TODO compare with the maximum subarray the Kadane's algorithm

"""


class Solution:
    def maxProduct(self, nums):

        # ! initialization
        # ! max so far
        maxSF = nums[0]
        # ! min so far
        minSF = nums[0]
        result = maxSF

        for i in range(1, len(nums)):
            curr = nums[i]
            # ! why need minSF?
            # ! when we encounter one negative number, we expect to get another negative number to make it positive
            # ! when we encounter one zero, no what we will get, it will still remian 0, \
            # ! however, we have no idea whether we will meet one negative number to make the current postive max product negative.
            # ! and this is the reason we define maxSF max so far and minSF min so far
            tmpmax = max(curr*maxSF, curr*minSF, curr)
            minSF = min(curr*maxSF, curr*minSF, curr)
            maxSF = tmpmax
            result = max(result, maxSF)

        return result
