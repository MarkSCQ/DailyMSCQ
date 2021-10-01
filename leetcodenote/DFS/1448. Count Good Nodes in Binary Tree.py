"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

            3
        1       4   
       3       1  5 
Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.


        3   
    3
   4 2
Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.


Key Points:
1. Do something with the current node
2. Add the current node's children to the stack or queue being used for the traversal
3. Move on to the next node
"""

# Definition for a binary tree node.


import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:

    def helper(self, root, maxSf):
        if root is None:
            return 0
        good = 1 if root.val >= maxSf else 0
        maxSf = max(root.val, maxSf)

        return good+self.helper(root.left, maxSf)+self.helper(root.right, maxSf)

    def goodNodes(self, root):
        # root maxsf, nodes amount
        return self.helper(root, float("-inf"))


class Solution2:

    def goodNodes(self, root):
        stack = [(root, float("-inf"))]
        good = 0
        while len(stack) != 0:

            root, maxsf = stack.pop()

            if maxsf <= root.val:
                good += 1
            if root.left:
                stack.append((root.left, max(root.val, maxsf)))

            if root.right:
                stack.append((root.right, max(root.val, maxsf)))
        return good


class Solution3:
    def goodNodes(self, root):
        queue = deque([(root, float("-inf"))])
        good = 0
        while len(queue) != 0:
            root, maxsf = queue.popleft()
            if maxsf <= root.val:
                good += 1
            if root.right:
                queue.append((root.right, max(root.val, maxsf)))
            if root.left:
                queue.append((root.left, max(root.val, maxsf)))
        return good
