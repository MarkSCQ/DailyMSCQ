"""
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

"""


# class Solution:
# def rob(self, nums):
def rob(nums):
    # ! adding one extra 0 will help with calculation
    helper = [0 for i in range(len(nums)+1)]
    # ! assign number[0] to helper[1] for inilization purpose
    helper[1] = nums[0]

    for i in range(2, len(helper)):
        # ! helper[i-1]: previous highest record
        # ! helper[i-2]+num[i-1]: previous previous record + current home. The reason of using i-1 here is that 
        # ! we use one extra 0 at the head, so we need to minus one to keep pace with the original array
        helper[i] = max(helper[i-1], helper[i-2]+nums[i-1])
    return max(helper)


nums = [2, 7, 9, 3, 1]
rob(nums)
