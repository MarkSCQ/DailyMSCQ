class Solution:
    def minSubArrayLen(self, target, nums):

        left = 0
        right = 0

        curr = len(nums)+1

        currsum = 0
        while right < len(nums):
            currsum = currsum+nums[right]

            while currsum >= target:
                curr = min(curr, right-left+1)
                currsum = currsum-nums[left]
                left = left+1
            right += 1
        
        if curr <= len(nums):
            return curr
        return 0
