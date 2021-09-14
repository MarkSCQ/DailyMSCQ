'''
NOTE:
1. Python create class format

    class objectName(object):
        def __init__(self,val):
            self.val=val
            self.next = None

2. when k==0: output 0

3. the input format
    for list: list(map(int, input().split()))
    for value: input()

'''



class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def listCreate(data):
    dummy = Node(-1)
    dummycp = dummy
    for i in range(len(data)):
        dummycp.next = Node(data[i])
        dummycp = dummycp.next
    return dummy.next


def lastKthNode(head, k):
    slow = head
    fast = head
    if k==0:
        print(slow.val)
        return
    for i in range(k):
        fast = fast.next

    while fast != None:

        slow = slow.next
        fast = fast.next
    print(slow.val)


def printList(head):
    while head != None:

        print(head.val)
        head = head.next


while True:
    nodeAmount = int(input())

    nodeVal = list(map(int, input().split()))

    Kval = int(input())

    head = listCreate(nodeVal)

    lastKthNode(head, Kval)


