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


def printPre(root):
    stack = []
    while root != None or len(stack) != 0:
        while root != None:
            stack.append(root)
            print(root.value)
            root = root.left
        root = stack.pop()
        root = root.right


def printRecursiveIn(root):
    if root == None:
        return None
    printRecursiveIn(root.left)
    print(root.value)
    printRecursiveIn(root.right)


def printIn(root):
    stack = []
    values = []

    stack = []
    while root != None or len(stack) != 0:
        while root != None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        print(root.value)
        root = root.right

def printRecursivePost(root):
    if root == None:
        return None
    printRecursivePost(root.left)
    printRecursivePost(root.right)
    print(root.value)


def printPost(root):
    stack = []
    pre = None

    while root != None or len(stack) != 0:
        while root != None:
            stack.append(root)
            root = root.left
        root = stack[-1]

        if root.right != None and root.right != pre:
            root = root.right
        else:
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
