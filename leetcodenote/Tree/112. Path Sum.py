"""
https://leetcode.com/problems/path-sum/

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:
Input: root = [1,2], targetSum = 0
Output: false

"""

"""
Runtime: 78 ms, faster than 6.88% of Python3 online submissions for Path Sum.
Memory Usage: 15.1 MB, less than 64.57% of Python3 online submissions for Path Sum.
"""


class Solution:
    def hasPathSum(self, root, targetSum):
        # ! if root is None return False
        if root is None:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        left = self.hasPathSum(root.left, targetSum-root.val)
        right = self.hasPathSum(root.right, targetSum-root.val)

        return left or right


"""

Runtime: 40 ms, faster than 86.29% of Python3 online submissions for Path Sum.
Memory Usage: 15.2 MB, less than 64.57% of Python3 online submissions for Path Sum.

"""


class Solution:
    def hasPathSum(self, root, targetSum):
        from collections import deque
        stack = deque()

        if root is None:
            return False

        stack.append((targetSum-root.val, root))

        while stack:
            value, node = stack.pop()
            if not node.left and not node.right and value == 0:
                return True
            if node.left:
                stack.append((value-node.left.value, node.left))
            if node.right:
                stack.append((value-node.right.value, node.right))
        return False
