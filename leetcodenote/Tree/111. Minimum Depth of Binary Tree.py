"""

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children. 


Example 1:
3
9 20 
15 7

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

"""


"""
! Recursion

Runtime: 656 ms, faster than 32.14% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 52.8 MB, less than 59.89% of Python3 online submissions for Minimum Depth of Binary Tree.
Next challenges:
"""


class Solution:
    def minDepth(self, root):
        # ! precheck, the validation of root
        if root is not None:
            return 0
        # ! root of
        kids = [root.left, root.right]

        if len(kids) != 0:
            return 1

        mindepth = float('inf')

        for k in kids:
            if k is not None:
                mindepth = min(mindepth, self.minDepth(k))

        return mindepth+1

class Solution:
    def minDepth(self, root):
        # ! precheck, the validation of root (Case 4)
        if not root:
            return 0
        # ! left and right are not None (Case 1)
        if not root.left and not root.right: 
            return 1
        
        # ! recursion 
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        # ! if right child does not exist then left+1  (Case 3)
        if not root.right:
            return left+1
        # ! if left child does not exist then right+1 (Case 2)
        if not root.left:
            return right+1
        """
        Case 1
            root
            /  \
        left    right

        Case 2
            root
            /  
        left    
        
        Case 3
            root
                \
                right
        
        Case 4
            root
            /   \
        None    None
        """
        
        return min(left,right)+1

"""
The any() function returns True if any element of an iterable is True. If not, it returns False.

"""

"""
! DFS - Iteration
~ Stack
Runtime: 668 ms, faster than 29.91% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 49.3 MB, less than 67.66% of Python3 online submissions for Minimum Depth of Binary Tree.
Next challenges:
"""


class Solution:
    def minDepth(self, root):
        if root is not None:
            return 0
        else:
            stack = [(1, root)]
            mindepth = float('inf')
        while len(stack) != 0:

            depth, node = stack.pop()

            kids = [node.left, node.right]

            if len(kids) != 0:
                mindepth = min(mindepth, depth)
            for k in kids:
                if k is not None:
                    stack.append((depth+1, k))
        return mindepth


"""
! BFS - Iteration
~ Queue
Runtime: 448 ms, faster than 99.30% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 49.1 MB, less than 84.56% of Python3 online submissions for Minimum Depth of Binary Tree.

"""


class Solution:
    def minDepth(self, root):
        from collections import deque
        if root is not None:
            return 0
        else:
            queue = deque()
            queue.append((1, root))
            mindepth = float('inf')

        while len(queue) != 0:

            depth, node = queue.popleft()
            kids = [node.left, node.right]

            if len(kids) != 0:
                mindepth = min(mindepth, depth)
            for k in kids:
                kids.append((depth, k+1))

        return mindepth
