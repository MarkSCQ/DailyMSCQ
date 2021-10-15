"""
https://leetcode.com/problems/perfect-squares/

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.


Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""


"""
Example of questions n=12

            1^2              2^2                3^2     4^2
            1                4                  9       16(X)
       _____|__              |_________
      |   |    |             |        |
    1^2  2^2  3^2           1^2       2^2
    3     5    10            5         8
          *                  *
    two *, 5 repeated

bottom up solution 

"""


class Solution:
    def numSquares(self, n):
        
        sqnum = [i**2 for i in range(0,int(n**0.5)+1)]
        
        dp = [float('inf')]*(n+1)
        
        dp[0]=0
        
        for i in range(1,n+1):
            for q in sqnum:
                if i<q:
                    break
                dp[i]=min(dp[i],dp[i-q]+1)
        return dp[-1]


def numSquares( n):
    # ! sqsum store the square numbers from 0 to n^0.5
    sqnum = [i**2 for i in range(0,int(n**0.5)+1)]
    # ! dp store the minimum number required for current index number. 
    # ! for example, when index=3, dp[3]=3, we need three one to make perfect queqre
    dp = [n]*(n+1)
    
    dp[0]=0

    for i in range(1,n+1):
        for q in sqnum:
            if i<q:
                break
            # print(i,q,i-q)
            # print(dp[i],dp[i-q]+1)
            # print(dp)
            # print("--------------------------------")
            dp[i]=min(dp[i],dp[i-q]+1)
    return dp[-1]

numSquares(12)