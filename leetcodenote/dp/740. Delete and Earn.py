"""
https://leetcode.com/problems/delete-and-earn/

Based on this tutorial: https://www.youtube.com/watch?v=YzZd-bsMthk

You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.



Example 1:
Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Example 2:
Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.


"""

"""
! This question can be translated to Leetcode 198 House Robber.
! 1. the question mentioned that when we take away nums[i] we will earn nums[i] points, the elements equal to nums[i]-1 and nums[i]+1 will be remove
! 2. the House Robber, the theif cannot steal two adjunct houses, which means that thief must make a choice between current and previous.
! 3. the input of this question can be translated into this format [0, 2*2, 3*3,4], if we select 3*3 then we cannot choose 2*2 or 4
! 4. the steps of this problem is 
    ~ A Translate input to the robber house format
    ~ B Apply Robber House to this question


"""


class Solution:

    def deleteAndEarn(self, nums):
        # ! robber house problem 
        def rob(nums):
            dp2 = 0
            dp1 = 0
            for i in range(len(nums)):
                dp = max(dp2+nums[i],dp1)
                dp2 = dp1
                dp1 =dp
            return dp1

        # ! length check
        if len(nums) == 0:
            return 0

        # ! translate the input to house robber input
        maxnum = max(nums)
        helper = [0 for i in range(maxnum+1)]
        # ! apply format as [0, 2*2, 3*3,4]
        for i in range(len(nums)):
            helper[nums[i]] += nums[i]


        return rob(helper)
