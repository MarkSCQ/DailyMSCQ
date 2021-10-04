"""
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.


Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false


! Intuition and Analysis
! 
! using recursion to simulate the process of searching for the bucket
! 
"""

class Solution:

    # ! using recursion to search
    def canPartition(self, itertionStart, nums, used, k, inProgressBucketSum, targetBucketSum):
        # ! recursion, when k is 1,
        # ! either the input k is 1 and of course, any array which is not None can be divided by 1
        # ! or it denotes, we keep using recursion to search, and the k is being keeping decreasing, since we need to decrease k by 1 when we get one valid array
        if k == 1:
            return True
        # ! when the sum we are processing is equal to targetBucketSum, this means we have finished finding one possible solution subset, 
        # ! k-1, because we have found one subset, decrease k by one
        # ! reset inProgressBacketSum to 0, because the current subset has been finished 
        if inProgressBucketSum == targetBucketSum:
            return self.canPartition(0, nums, used, k-1, 0, targetBucketSum)
        # ! if the current inProgressBacketSum cannot satisfy the check above, then we start seaching
        # ! starting searching at the iteration start 
        for i in range(itertionStart, len(nums)):
            # ! used arrya is used to mark the elements that have been uesd in the previous operations
            # ! if the number has not been used, then mark it as True
            if not used[i]:
                used[i] = True
                # ! recursion checking whether the subset exists. nums[i] has been used, starting index+1
                # ! inProgressBuckedSum + nums[i], which is the number being used in this round
                if self.canPartition(i+1, nums, used, k, inProgressBucketSum+nums[i], targetBucketSum):
                    return True
                # ! after being used, mark the current number as False
                used[i] = False
        # ! if all numbers can be used then they must have hit the k==1
        # ! otherwise, return False to mark that it cannot be partioned
        return False

    def canPartitionKSubsets(self, nums, k):
        # ! get sum of nums
        numsSum = sum(nums)
        # ! Precheck
        # ! if k is 0 or the current sum of nums cannot be divied by k, 
        # ! then return because it cannot be divied
        if k == 0 or numsSum % k != 0:
            return False
        # ! start partition with 
        # ! itertionStart = 0, the starting index of the nums array
        # ! nums, original input 
        # ! used, initialized as the same size as input
        # ! k the target division factor
        # ! inProgressBacketSum, current process sum amount
        # ! targetBucketSum, the number we get by using sum//k
        return self.canPartition(0, nums, [0 for i in range(len(nums))], k, 0, numsSum//k)
