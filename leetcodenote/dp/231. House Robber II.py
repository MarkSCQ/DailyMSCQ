"""
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3
"""

"""
! Similar to the robber one question, the difference is 
! 1. this question the houses are placed in a circle
! 2. we need to consider two situations,
!       -> If start at 0, the ending is len-2
!       -> If Start at 1, the ending is len-1
! 3. Finally get the max of solution 0 and solution 1


"""


class Solution:

    def rob(self, nums: List[int]) -> int:
        def fun(nums,starting,ending):
            
            rnums = []
            for i in range(starting,ending+1):
                rnums.append(nums[i])
            
            helper=[0 for i in range(len(rnums)+1)]
            helper[1]=rnums[0]
            
            for i in range(2,len(rnums)+1):
                
                helper[i]=max(helper[i-2]+rnums[i-1],helper[i-1])
            return helper[-1]
        
        lnums = len(nums)
        
        if lnums==0:
            return 0
        if lnums==1:
            return nums[0]
        
        max1 = fun(nums,0,lnums-2)
        max2 = fun(nums,1,lnums-1)
        
        
        return max(max1,max2)


