"""
https://leetcode.com/problems/sliding-window-maximum/
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.


Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,-1], k = 1
Output: [1,-1]

Example 4:
Input: nums = [9,11], k = 2
Output: [11]

Example 5:
Input: nums = [4,-2], k = 2
Output: [4]

"""

"""
Solution: Monotonic Queue
class MonotonicQueue{

    public：
    * push an element on the queue
    * will pop all elements smaller than e 
    void push(int e);
    * pop the max element
    void pop();
    int max() const;
}

"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        # ! precheck
        if len(nums)*k == 0:
            return []
        if k == 1:
            return nums

        # ! apply monotonic queue, using queue to simulate
        from collections import deque
        # ! monodeque store index, res store element value
        monodeque = deque()
        res = []
        # ! iterate every element
        for i in range(len(nums)):
            # ! if the monotionic queue is not empty and the tail element of queue is smaller than the current element, pop the element. If he last element of monotonic is bigger, then keep it. 
            while len(monodeque) != 0 and nums[monodeque[-1]] <= nums[i]:
                monodeque.pop()
            # ! add the current element(index) to the queue
            monodeque.append(i)

            # ! monodeque store index values, monodeque[0], the previous added element
            # ! i-k i is the current element, k is the size of window. i-k is the limit for the window
            # ! if the index is equal to i-k, then it means it will be out of boundary of the window.
            if monodeque[0] == i-k:
                monodeque.popleft()
            # ! if window has k elements, then (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
            if i >= k-1:
                res.append(nums[monodeque[0]])
        return res


# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         from collections import deque
#         q = deque()  # stores *indices*
#         res = []
#         for i, cur in enumerate(nums):
#             print(i, " ", cur)
#             while q and nums[q[-1]] <= cur:
#                 q.pop()
#             q.append(i)
#             # remove first element if it's outside the window
#             if q[0] == i - k:
#                 q.popleft()
#             # if window has k elements add to results (first k-1 windows have < k elements because we start from empty window and add 1 element each iteration)
#             if i >= k - 1:
#                 res.append(nums[q[0]])
#         return res
