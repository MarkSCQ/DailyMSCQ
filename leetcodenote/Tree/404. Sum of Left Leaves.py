"""
https://leetcode.com/problems/sum-of-left-leaves/

Given the root of a binary tree, return the sum of all left leaves.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:
Input: root = [1]
Output: 0
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
BFS
"""


class Solution:
    def sumOfLeftLeaves(self, root):
        sm = 0

        from collections import deque

        if not root:
            return 0

        queue = deque([(root, 0)])

        while queue:

            root, flg = queue.popleft()

            if flg == 1 and root.left is None and root.right is None:
                sm += root.val
            else:
                if root.left:
                    queue.append((root.left, 1))
                if root.right:
                    queue.append((root.right, 0))

        return sm


"""
DFS
"""


class Solution:
    def sumOfLeftLeaves(self, root):
        sm = 0

        if not root:
            return 0
        stack = [root]

        while stack:
            node = stack.pop()

            if node.left is not None and node.left.left is None and node.left.right is None:
                sm += node.left.val

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return sm
