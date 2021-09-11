# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def inorderTraversal(self, root):
        stack = []
        value = []
        while len(stack) != 0 or root != None:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            value.append(root.val)
            root = root.right
        return value


class Solution2:
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
