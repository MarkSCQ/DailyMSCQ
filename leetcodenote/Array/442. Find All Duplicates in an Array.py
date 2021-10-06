"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []

"""

"""
dict as a map
Store Seen Elements in a Set / Map

"""


class Solution:
    def findDuplicates(self, nums):
        res = set()
        data = {}

        for i in range(len(nums)):
            if nums[i] not in data:
                data[nums[i]] = 1
            else:
                data[nums[i]] += 1

            if data[nums[i]] > 1:
                res.add(nums[i])
        return res


"""
list as a map
Store Seen Elements in a Set / Map

"""


class Solution:
    def findDuplicates(self, nums):
        res = [0 for i in range(max(nums)+1)]

        for i in range(len(nums)):
            res[nums[i]] += 1

        re = []
        for i in range(len(res)):
            if res[i] > 1:
                re.append(i)

        return re


"""
Notice that it only appears at most twice
"""


class Solution:
    def findDuplicates(self, nums):
        res = []

        nums.sort()
        i = 1

        while i < len(nums):
            if nums[i] == nums[i-1]:
                res.append(nums[i])
                # ! Skip the duplicated elements
                i += 1
            i += 1
        return res
