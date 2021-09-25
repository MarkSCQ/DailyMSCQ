"""
https://leetcode.com/problems/two-sum-less-than-k/

1099. Two Sum Less Than K

Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

Example 1:

Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: nums = [10,20,30], k = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less that 15.

"""


"""
Two Pointer
1 sort
2 if current sum < k, head+=1 else tail-=1

"""

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        snums = sorted(nums)
        
        head= 0
        tail=len(snums)-1
        curr = -1
        
        while head<tail:
            sm = snums[head]+snums[tail]
            if sm<k:
                curr = max(sm,curr)
                head+=1
            else:
                tail-=1
                
        return curr