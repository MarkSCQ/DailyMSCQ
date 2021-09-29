"""
https://leetcode.com/problems/middle-of-the-linked-list/
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""


class Solution:
    def middleNode(self, head):
        fast = head
        slow = head

        while fast != None or fast.next != None:

            if fast.next == None or fast.next.next == None:
                break
            elif fast.next.next != None:
                slow = slow.next
                fast = fast.next.next
        if fast.next != None:
            return slow.next
        return slow


"""
! Modified version 
! Notice the and and or conditions

"""
class Solution1:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow