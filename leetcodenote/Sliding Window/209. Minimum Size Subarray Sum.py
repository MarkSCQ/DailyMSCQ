"""
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


"""



"""
! NOTICE
!   1. subarray is continuous; 
!   2. equal or greater
!   3. all elements in the array are bigger or equal than 0, (!!!!! this is very important)
! Sliding window
!   
!   

"""


class Solution:
    def minSubArrayLen(self, target, nums):

        # ! two edge of window, left shrink to right, right will extend to right
        left = 0
        right = 0

        curr = len(nums)+1

        currsum = 0

        while right < len(nums):
            # ! current sum within the window
            currsum = currsum+nums[right]
            # ! if current sum is bigger than target 
            while currsum >= target:
                # ! calculate the current window length and compare with the existing window
                # ! then assign the minimum of them as the new curr minimum 
                curr = min(curr, right-left+1)
                # ! the current right and left meet the requiremnts, 
                # ! however, we do not know whether tne next elements we take will make currsum>=target
                # ! and most of important, we want to have the minimum size of subarry, 
                # ! and we have no idea whether the current is the minimum, 
                # ! based on this situation, we shrink the left to right,
                currsum = currsum-nums[left]
                left = left+1
            # ! after checking the left edge, right move forward
            right += 1
        
        if curr <= len(nums):
            return curr
        return 0
