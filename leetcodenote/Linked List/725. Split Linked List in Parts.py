"""


"""


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def llSize(head):
            
            length = head
            count=0

            while length!=None:
                count+=1
                length=length.next
            return count
        
        llen = llSize(head)
        l = llen//k
        r = llen%k
        
        ans=[None for i in range(k)]
        h1 = head
        prev = None
        for i in range(k):
            ans[i]=head
            partlen = l
            if r>0:
                partlen+=1
            for j in range(partlen):
                prev=head
                head=head.next
            if prev!=None:
                prev.next=None
            r-=1
        return ans
   
        