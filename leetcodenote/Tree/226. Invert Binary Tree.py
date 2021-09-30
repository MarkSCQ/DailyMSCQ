# 226 Invert Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        if root is None:
            return None

        # ! initialize the queue to help with the node storage
        # ! queue, first in, first out/
        queue = []
        queue.append(root)

        while len(queue) != 0:
            # ! pop out the node at head and exchange its left and right child
            curr = queue.pop(0)
            tmp = curr.left
            curr.left = curr.right
            curr.right = tmp
            # ! for current node, if left sub tree is not None, add the left to queue
            if curr.left is not None:
                queue.append(curr.left)
            # ! for current node, if right sub tree is not None, add the right to queue
            if curr.right is not None:
                queue.append(curr.right)

        return root

    def invertTree(self, root):
        if root is None:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
