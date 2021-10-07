"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]

"""


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Iteration
"""

# ! Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]


class Solution:
    def buildTree(self, inorder, postorder):
        # ! root, current subtree root
        # ! stack, store nodes we created in postorder
        # ! index, pointer to inorder data list
        root, stack, index = None, [], 0
        for val in reversed(postorder):
            new_node = TreeNode(val)
            if not root:
                # ! root of the tree we are going to create doesnt exist, we then create the tree root
                # ! assign the root to node for the usage of creating left and right children
                node = root = new_node
            else:
                # ! ~ Inverts all the bits,
                # ! ~0=>-1  ~1=>-2  ~-2=>1
                # ! Searching the left subtree
                # ! if the value of current node is equal to the value at tail of inorder
                if node.val == inorder[~index]:
                    # ! the stack is used to store the nodes that have been created in reversed post ordered
                    # ! if the top element which is the node created in the previous round is equal to the reversed index in inorder
                    # ! this means we are now need to pop elements to reach the root of current subtree
                    while stack and stack[-1].val == inorder[~index]:
                        index += 1
                        node = stack.pop()
                    # ! once we reach the root of current subtree, assign the left child
                    node.left = new_node
                    node = new_node
                else:
                    # ! Searching the right subtree
                    node.right = new_node
                    node = new_node
            # ! store the created nodes
            stack.append(new_node)
        return root


"""
Runtime: 56 ms, faster than 87.12% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 17.8 MB, less than 99.26% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
"""


"""
Recursion
"""


class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        # ! pop the last elements of postorder as root value
        root = TreeNode(postorder.pop())
        # ! find the slice point in inorder
        mid = inorder.index(root.val)
        # ! assign two data that contains left and right data.
        # ! Notice the pop() function has removed the root data in postorder
        root.right = self.buildTree(inorder[mid+1:], postorder)
        root.left = self.buildTree(inorder[:mid], postorder)

        return root


"""

Runtime: 132 ms, faster than 50.05% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 53.2 MB, less than 39.17% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.

"""
