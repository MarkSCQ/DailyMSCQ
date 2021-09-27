"""
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.

Example 2:
Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.

Example 3:
Input: arr = [1,2,3,4,5,6,7]
Output: 16

"""

"""

we would like to know how manysubarrays end with arr[i] have odd or even sums.

dp[i][0]  end with arr[i] has odd sum
dp[i][1]  end with arr[i] has even sum 


for example we have an array 1 2 3 4 5 6, lets start from 4

1 2 3 4
odd = [3,4] 
        [2,3,4]
even = [4] 
        [1,2,3,4]
dp[4][0]=2
dp[4][1]=2

add 5
1 2 3 4 5
odd = [4,5] 
        [1,2,3,4,5]
        [5]
even = [3,4,5] 
        [2,3,4,5]
dp[5][0]=2
dp[5][1]=2+1

add 6
1 2 3 4 5 6
odd = [5,6] 
        [4,5,6]
        [2,3,4,5,6]
even = [3,4,5,6] 
        [1,2,3,4,5,6]
        [6]

dp[6][0]=2+1
dp[6][1]=3

if arr[i] is even:
    dp[i][0]=dp[i-1][0]+1
    dp[i][1]=dp[i-1][1]
else:
    dp[i][0]=dp[i-1][1]
    dp[i][1]=dp[i-1][0]+1

if we add one even number to the current list, the current even will change, but the current odd remain what it was
if we add one odd number to the current list, the current odd will change , but the current even will remain tge same


if the current accu sum is odd, we care only about previous even accu sums and vice versa.

"""


class Solution:
    def numOfSubarrays(self, arr):
        count = 0

        # +1 avoid boundary error
        dp = [[0, 0] for i in range(len(arr)+1)]

        for i in range(1, 1+len(arr)):
            if arr[i-1] & 1:
                # ! if odd
                dp[i][0] = dp[i-1][1]
                dp[i][1] = dp[i-1][0] + 1
            else:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][1] = dp[i-1][1]
            count += dp[i][1]

        return count % (10**9 + 7)
