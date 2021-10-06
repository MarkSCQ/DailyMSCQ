"""
https://leetcode.com/problems/flip-equivalent-binary-trees/

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivelent or false otherwise.

Example 1:

Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.

Example 2:
Input: root1 = [], root2 = []
Output: true

Example 3:
Input: root1 = [], root2 = [1]
Output: false

Example 4:
Input: root1 = [0,null,1], root2 = []
Output: false

Example 5:
Input: root1 = [0,null,1], root2 = [0,1]
Output: true
"""

"""
Intuition

Recursion get the l1 l2 r1 r2 value, these values are bool values from three returns

Example:

    1         1
   / \       / \
  2   3     3   2

l1 = self.flipEquiv(root1.left, root2.left)    
    =>  2 and 3 
    =>  2 left and rignt are None
    =>  3 left ande right are None
    =>  2!=3 
    =>  bool(None)=False bool(not None)=True
    =>  root1.val=2 != root2.val=3 
    =>  return False

l2 = self.flipEquiv(root1.left, root2.right)   
    => 2 and 2
    =>  ...
    =>  return True

r1 = self.flipEquiv(root1.right, root2.right)  
    =>  3 and 2 
    =>  ...
    =>  return False

r2 = self.flipEquiv(root1.right, root2.left)
    =>  3 and 3
    =>  ...
    => return True

root1.val==root2.val==1  l1 and r1 == False l2 and r2 == True
            ||                   || l           ||
root1.val == root2.val and ((l1 and r1) or (l2 and r2))

"""


class Solution:
    def flipEquiv(self, root1, root2):
        # ! if root1 and root2 are both None return True
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        l1 = self.flipEquiv(root1.left, root2.left)
        l2 = self.flipEquiv(root1.left, root2.right)

        r1 = self.flipEquiv(root1.right, root2.right)
        r2 = self.flipEquiv(root1.right, root2.left)

        return root1.val == root2.val and ((l1 and r1) or (l2 and r2))
