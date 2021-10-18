"""
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).


Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
"""


"""

prefix sum and preorder
prefix sum -> dictionary, hash maping realtionship
example 3 4 1 6 -3
[prefix sum: frequency]
{3:1,7:1,8:1,14:1,11:1}

class So
    def subarraySum(self, nums, k):
        count = curr_sum = 0
        h = defaultdict(int)
        
        for num in nums:
            # current prefix sum
            curr_sum += num
            
            # situation 1:
            # continuous subarray starts 
            # from the beginning of the array
            if curr_sum == k:
                count += 1
            
            # situation 2:
            # number of times the curr_sum − k has occurred already, 
            # determines the number of times a subarray with sum k 
            # has occurred up to the current index
            count += h[curr_sum - k]
            
            # add the current sum
            h[curr_sum] += 1
                
        return count

preorder 
mid-> left subtree -> right subtree


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root, sum):

        def preorder(node, curr_sum):
            nonlocal count
            if not node:
                return
            # ! continue adding node's value
            curr_sum += node.val
            # ! if curr_sum == k, counter+1
            if curr_sum == k:
                count += 1
            # ! if curr_sum-k exists, then k must exists. h[curr_sum-k] denotes this situation
            # ! `if curr_sum-k not exits, then count will add 0, 
            count += h[curr_sum - k]
            # ! below, increase the counter of curr_sum
            h[curr_sum] += 1

            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            
            h[curr_sum] -= 1
        
        count = 0
        k = sum

        from collections import defaultdict
        # ! using defaultdict(int) when assign a key without a value, the value will be initialized with 0
        h = defaultdict(int)
        
        preorder(root, 0)
        return count
