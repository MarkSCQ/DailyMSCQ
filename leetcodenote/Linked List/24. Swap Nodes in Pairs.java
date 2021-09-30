// class Solution {

//     public ListNode ReverseAtoB(ListNode A, ListNode B) {
//         // next and prev are pointers that move forward
//         ListNode prev = null
//         ListNode curr = A
//         ListNode next = null

//         while (curr != B) {
//             // next move to next
//             next = curr.next
//             // reverse
//             curr.next = prev
//             // reset prev and curr pointers
//             prev = curr
//             curr = next
//         }
//         return prev
//     }

//     public ListNode swapPairs(ListNode head) {

//         ListNode node_a = head
//         ListNode node_b = head
//         for(int i=0
//             i < 2
//             i++)
//         {
//             if(node_b == null)
//             return head
//             node_b = node_b.next
//         }

//         ListNode nh = ReverseAtoB(node_a, node_b)
//         node_a.next = swapPairs(node_b)

//         return nh
//     }
// }
