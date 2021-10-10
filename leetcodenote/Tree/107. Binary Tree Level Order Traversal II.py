"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrderBottom(self, root):
        from collections import deque
        ans = []
        queue = deque()

        if not root:
            return []
        queue.append(root)
        level = 0
        while queue:
            curr = []
            for i in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(curr)
        return ans[::-1]
