"""
https://leetcode.com/problems/koko-eating-bananas/

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23


"""

"""
Intuition

Using binary search.
Searching Range (left,right)
    left =1
    right = max(piles)
    mid = left+(right-left)//2

iteration, comparing the hours using mid with given hours h
if smaller, go to left section
else, go to right section

finally return left

"""




import math
class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        res = right

        def check(mid):
            hours = 0
            for i in piles:
                hours += math.ceil(i/mid)
                # hours += (i+mid-1)//mid
            return hours

        while left <= right:

            mid = left+(right-left)//2

            if check(mid) <= h:
                res = min(res, mid)
                right = mid-1
            else:
                left = mid+1
        return res


class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left < right:
            mid = left+(right-left)//2
            hours = 0
            for i in piles:
                hours += (i+mid-1)//mid
            if hours <= h:
                right = mid
            else:
                left = mid+1

        return left
