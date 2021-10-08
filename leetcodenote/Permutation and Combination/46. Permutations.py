"""
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

"""


"""
Backtracking
Structure of this method
          [1,2,3]
        /    |    \
    [2,3]  [1,2]  [1,3]
    /  |    / \     | \
  [2] [3] [1] [2]  [1] [3]

"""


class Solution:
    def permute(self, nums):
        # ! store resutls
        res = []
        # ! using recursion, when nums has only one element
        if len(nums) == 1:
            return [nums[:]]

        # ! for each number in the nums, doing permutation
        for i in range(len(nums)):
            # ! extract the first element of the nums
            n = nums.pop(0)
            # ! recursively calling the function to make permutations
            perms = self.permute(nums)
            # ! for each permutation pairs, add the popped element at tail
            for i in range(len(perms)):
                perms[i].append(n)
            # ! adding current number's permutations to the results
            res.extend(perms)
            # ! recover
            nums.append(n)
        return res


"""
Heap's Algorithm

If the first integer to consider has index n that means that the current permutation is done.

Iterate over the integers from index first to index n - 1.
    lace i-th integer first in the permutation, i.e. swap(nums[first], nums[i]).
    Proceed to create all permutations which starts from i-th integer : backtrack(first + 1).
    Now backtrack, i.e. swap(nums[first], nums[i]) back.
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first=0):
            # if all integers are used up
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output
