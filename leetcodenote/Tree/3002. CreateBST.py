"""
Create a BST 
"""

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def createBST(nums):
    root = None
    for num in nums:
        root = insert(root, num)
    return root


# ! insert one value using recursion, the recursion here is mainly used for searching the appropriate insertion position
def insert(root, value):
    # ! base case, create node that holdes value
    if not root:
        return TreeNode(value)
    # ! value check
    if value <= root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)


if __name__ == '__main__':
    root=createBST([5,3,1,4,7,6])
    inorder(root)
