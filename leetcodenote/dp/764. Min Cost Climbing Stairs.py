"""


https://leetcode.com/problems/min-cost-climbing-stairs/


You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].

这题的意思 说人话，

top就是list尾部，len(num)
每一个element代表了当前这个台阶所需要的代价。
假设 1 100 1 1， 那么从第一个台阶到最后需要怎么算呢？

从第三个台阶开始 min(cost[i-1],cost[i-2])， 我们只需要取两者最小值即可


"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2,len(cost)):
            cost[i]+=min(cost[i-1],cost[i-2])
        return min(cost[-1],cost[-2])