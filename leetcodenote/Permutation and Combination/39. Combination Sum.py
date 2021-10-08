"""

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]

"""


# ! Example 39. Combination Sum Example.png

"""
Backtracking and DFS



"""


class Solution:
    def combinationSum(self, candidates, target):
        res = []
        # ! index tracking the element;
        # ! curr the elements taken into consideration
        # ! the current element sum

        def dfs(index, curr, total):
            # ! add to results if current sum is equal to target
            if target == total:
                res.append(curr[:])
                return

            # ! index>=len(candidates) out of boundary
            # ! total>target  not meets the target requirements
            if index >= len(candidates) or total > target:
                return
            # ! curr array is used to tracked the resutls
            curr.append(candidates[index])
            # ! trial, if adding current element will meet the requirements
            dfs(index, curr, total+candidates[index])
            # ! recover the previous added elements
            curr.pop()
            # ! trial, if skipping the current element will meet the requirements
            dfs(index+1, curr, total)

        dfs(0, [], 0)

        return res
