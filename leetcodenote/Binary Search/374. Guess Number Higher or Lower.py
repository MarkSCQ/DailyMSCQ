"""
https://leetcode.com/problems/guess-number-higher-or-lower/


We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.

 

Example 1:
Input: n = 10, pick = 6
Output: 6

Example 2:
Input: n = 1, pick = 1
Output: 1

Example 3:
Input: n = 2, pick = 1
Output: 1

Example 4:
Input: n = 2, pick = 2
Output: 2


"""

"""
Binary Search is faster than the second Ternary Search
"""


class Solution:
    def guessNumber(self, n):
        left = 1
        right = n

        while left <= right:

            mid = left+(right-left)//2

            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                left = mid+1
            elif res == -1:
                right = mid-1


class Solution:
    def guessNumber(self, n):
        right = n

        while left <= right:

            mid1 = left+(right-left)//3
            mid2 = right-(right-left)//3

            res1 = guess(mid1)

            res2 = guess(mid2)

            if res1 == 0:
                return mid1
            if res2 == 0:
                return mid2

            if res1 == -1:
                right = mid1-1
            elif res2 == -1:
                right = mid2-1
            elif res1 == 1:
                left = mid1+1
            elif res2 == 1:
                left = mid2+1
