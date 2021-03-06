"""
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output:
[
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]

"""


# ! k is the length of each pair
# ! n is the range, from 1 to n
class Solution:
    def combine(self, n, k):

        def backtrack(first=1, curr=[]):
            # ! if the combination is done
            if len(curr) == k:
                output.append(curr[:])
            # ! first, the starting index
            for i in range(first, n + 1):
                # ! add i into the current combination
                curr.append(i)
                # ! use next integers to complete the combination
                backtrack(i + 1, curr)
                # ! backtrack
                curr.pop()

        output = []
        backtrack()
        return output


class Solution:
    def combine(self, n, k):
        res = []

        def makecomb(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            for i in range(start, n+1):
                comb.append(i)
                self.combine(start+1, comb)
                comb.pop()
                pass

        makecomb(1, [])
        return res
