"""

Given an integer array nums and two integers k and t, 
return true if there are two distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false


"""


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # abs(nums[i] - nums[j]) <= t and abs(i - j) <= k
        if t < 0:
            return False

        d = {}
        # ! avoid t=0
        w = t+1

        for i in range(len(nums)):
            # ! calculate bucked of current number
            m = nums[i]//w

            # ! check whether current element in the dic,
            # ! this dic is store the bucket
            # ! check the neighbours of current element's bucket
            if m in d:
                return True
            if m-1 in d and abs(nums[i]-d[m-1]) < w:
                return True
            if m+1 in d and abs(nums[i]-d[m+1]) < w:
                return True
            # ! if not exists in d, then assgin the bucket and number
            d[m] = nums[i]
            # ! delete element when i>=k, this means the window shifts
            if i >= k:
                del[d[nums[i-k]//w]]
        return False
