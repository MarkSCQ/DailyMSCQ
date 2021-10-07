"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]


Example 1 explanation

for any tree, the rules of these two orders are
    preorder => mid left right
    inorder => left mid right

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

by using the rules, 
we know root is 3 from preorder
in inorder data, by using root is 3, the left part is [9] the right part is [15 20 7]

        3
    [9]   [15 20 7]

according to preorder[20 15 7]
the root of this subtree is 20, two child is 15 and 7
in inorder data, 15 20 7, we know that the left child is 15, the right child is 7


"""
from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        # ! precheck
        if not preorder or not inorder:
            return None

        # ! get root from preorder data
        root = TreeNode(preorder[0])
        # ! get index of root element in preorder
        mid = inorder.index(preorder[0])
        # ! constructing root.left
        # ! preorder[1:mid+1] and inorder[:mid] are the data of left child
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # ! constructing root.right
        # ! preorder[mid+1:] and inorder[mid+1:] are the data of right child
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root,stack,index = None,[],0
        for val in reversed(postorder):
            new_node = TreeNode(val)
            if not root:
                node = root = new_node
            else:
                if node.val==inorder[~index]:
                    while stack and stack[-1].val == inorder[~index]:
                        index+=1
                        node=stack.pop()
                    node.left = new_node
                    node = new_node
                else:
                    node.right = new_node
                    node = new_node
            stack.append(new_node)
        return root


        