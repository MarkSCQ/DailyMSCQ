class Solution:
    def hasCycle(self, head):
        fast = head
        slow = head
        if head is None:
            return False
        if fast.next is None or fast.next.next is None:
            return False

        fast = fast.next.next
        while fast != slow:
            if fast.next is None or fast.next.next is None:
                return False
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next

        return True
