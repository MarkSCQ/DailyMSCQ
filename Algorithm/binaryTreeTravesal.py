class treeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def printRecursivePre(root):
    if root == None:
        return None
    print(root.value)
    printRecursivePre(root.left)
    printRecursivePre(root.right)


def printRecursiveIn(root):
    if root == None:
        return None
    printRecursiveIn(root.left)
    print(root.value)
    printRecursiveIn(root.right)


def printRecursivePost(root):
    if root == None:
        return None
    printRecursivePost(root.left)
    printRecursivePost(root.right)
    print(root.value)


def printPre(root):
    # ! store nodes
    stack = []
    while root != None or len(stack) != 0:
        # ! Preorder Root->leftChild->rightChild
        while root != None:
            # ! store current root's left child and left child's left descendents
            stack.append(root)
            print(root.value)
            root = root.left
        # ! when finish the left children/descendents storage
        # ! pop out the last one, the last added left descendent
        root = stack.pop()
        # ! after printing the left value in the nested while iteration,
        # ! reassign the root to the right
        root = root.right


def printIn(root):
    stack = []
    # ! if root is not none: the tree at lesat has one node;
    # ! if stack is not 0: meaning there are nodes stored in the stack
    while root != None or len(stack) != 0:
        # ! add all current left descedents to the stack,
        # ! while root is not none,
        # ! for example, previous rount print LEFT value,
        # ! however the left does not have any kids.
        # ! so this nested iteration will be skipped.
        # ! the root=stack.pop() will reassign Root as the new root
        # ~             ROOT
        # ~             /  \
        # ~         LEFT    RIGHT
        while root != None:
            stack.append(root)
            root = root.left
        # ! order leftChild, Root, rightChild
        # ! all left descendents have been added
        # ! pop the last one, which is the leftmost node
        root = stack.pop()
        print(root.value)
        root = root.right


def printPost(root):
    # ! stack store nodes
    stack = []
    # ! store previous node in the previous round(iteration)
    pre = None
    while root != None or len(stack) != 0:
        # ! store left descedents in the stack
        while root != None:
            stack.append(root)
            root = root.left
        # ! get the last added node
        root = stack[-1]
        # ! condition: check whether should go for the right node
        if root.right != None and root.right != pre:
            root = root.right
        else:
            # ! get value, pop old node, reset pre and root node
            print(root.value)
            stack.pop()
            pre = root
            root = None


def main():
    root = treeNode(1)
    l11 = treeNode(2)
    r11 = treeNode(3)

    l21 = treeNode(4)
    r22 = treeNode(5)
    l23 = treeNode(6)
    r24 = treeNode(7)

    root.left = l11
    root.right = r11

    l11.left = l21
    l11.right = r22

    r11.left = l23
    r11.right = r24

    # printRecursivePre(root)
    # print("==================================")
    # printPre(root)
    # print("==================================")
    # printRecursiveIn(root)
    printRecursiveIn(root)
    print("==================================")
    printIn(root)


if __name__ == '__main__':
    main()
