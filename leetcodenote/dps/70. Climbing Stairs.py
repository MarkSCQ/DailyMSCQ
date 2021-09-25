"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

!
!   1. mentioned in the question: each time can only take one step or two steps
!   2. these two different steps => two basic different situations 
!
"""

# ! fib using swap values


class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        prevv = 1
        prev = 2
        curr = 0

        for i in range(2, n):
            curr = prev+prevv

            prevv = prev
            prev = curr
        return curr


# ! fib using recursion
class Solution1:
    # ! work but time out
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n-1)+self.climbStairs(n-2)


# ! DP using array
class Solution2:
    def climbStairs(self, n):
        dp = [0, 1, 2]
        if n == 1:
            return dp[1]
        if n == 2:
            return dp[2]
        for i in range(3, n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[-1]


# ! fib recursion using memoization
cache = {}


class Solution:
    def climbStairs(self, n):
        if n in cache:
            return cache[n]
        if n < 4:
            return n
        else:
            output = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            cache[n] = output
        return output
