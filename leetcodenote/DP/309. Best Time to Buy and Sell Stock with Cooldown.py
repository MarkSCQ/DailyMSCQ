"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0

"""



"""
State machine. 

                  _________________________
                  |                       ^
                  V    buy        sell    |
                reset  ->   hold   ->   sold
                |  ^        |  ^
                V  |        V  |
                reset       reset 

Three different states transfer from each other.


"""


class Solution:
    def maxProfit(self, prices):
        hold = float('-inf')
        sold = 0
        reset = 0

        for p in prices:
            presold = sold
            sold = hold+p
            hold = max(hold, reset-p)
            reset = max(reset, presold)

        return max(sold, reset)
