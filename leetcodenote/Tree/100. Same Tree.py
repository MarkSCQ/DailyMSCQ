"""
https://leetcode.com/problems/same-tree/
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

"""

"""
Recursion
"""


class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)

        return p.val == q.val and l and r


"""
DFS
"""


class Solution:
    def isSameTree(self, p, q):

        stack = [(p, q)]
        while stack:

            pnode, qnode = stack.pop()

            if pnode and qnode and pnode.val == qnode.val:
                stack.append((pnode.left, qnode.left))
                stack.append((pnode.right, qnode.right))
            elif qnode or pnode:
                return False
        return True


"""
BFS
"""


class Solution:
    def isSameTree(self, p, q):
        from collections import deque

        queue = deque([(p, q)])
        while queue:

            pnode, qnode = queue.popleft()
            if not pnode and not qnode:
                continue
            if not pnode or not qnode:
                return False
            if pnode.val != qnode.val:
                return False

            if pnode:
                queue.append((pnode.left, qnode.left))
                queue.append((pnode.right, qnode.right))

        return True
