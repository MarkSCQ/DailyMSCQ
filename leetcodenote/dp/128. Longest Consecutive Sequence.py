"""
https://leetcode.com/problems/longest-consecutive-sequence/


Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

"""

"""
! solution 1
!    1. first sort the array
!    2. then find the consecutive array.
!    3. Since there might exist duplicated elements.
!        Using nums[i]!=nums[i-1] to avoid the duplicated scenarios.

"""


class Solution1:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        current = 1
        longest = 1

        nums.sort()

        for i in range(1, len(nums)):

            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    current += 1
                else:
                    longest = max(longest, current)
                    current = 1
        return max(longest, current)


"""
Solution 2

One of the requirements mentioned that the time complexity should be O(n).
Obviously, solution is olgn because we use sort() which takes olgn time


This solution is going to apply set. Each time check whether the current number from set satisfy the conditions.

"""


class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        longest = 0

        snums = set(nums)

        for num in snums:
            if num-1 not in snums:
                curr = num
                curr_streak = 1
                while curr+1 in snums:
                    curr_streak += 1
                    curr += 1
                longest = max(longest, curr_streak)

        return longest
