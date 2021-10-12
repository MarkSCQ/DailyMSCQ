"""
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


"""


"""
Two pointers, fix one element each time

"""
class Solution:
    def threeSum(self, nums )  :
        res = []
        
        # 1 sorting
        nums.sort()
        numslen = len(nums)
        for i in range(len(nums)):
            # ! remove duplicated elements
            if i!=0 and nums[i-1]==nums[i]:
                continue
            # ! two pointers
            left = i+1
            right = numslen-1

            while left<right:

                if nums[left]+nums[right]> -nums[i]:
                    right-=1
                elif nums[left]+nums[right]<-nums[i]:
                    left+=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    # ! two while remove duplicates
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1

                    left+=1
                    right-=1
        print(res)
        return res