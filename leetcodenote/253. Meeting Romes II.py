"""
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
"""

import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        free = []
        intervals.sort(lambda x: x[0])
        # ! notice: the heapq here is not normal queue, it's priority queue
        # ! priority queue the pop of it is based on the prigority.
        # ! when push elements to the heapq, it will not only push the element,
        # ! but also rearrange the order based on the priority of the queue
        heapq.heappush(free, intervals[0][1])
        for i in range(1, len(intervals)):
            print(free)
            if free[0] <= intervals[i][0]:
                # ! heappop will pop the element, this is based on the priority.
                # ! free[0] the earlist meeting's ending
                # ! if the earlist meeting's ending is smaller than the current element's beginning
                # ! then we will pop the first one.
                # ! when first end < second start, this means this first and second can be considered as one room
                heapq.heappop(free)
            heapq.heappush(free, intervals[i][1])
            print(free)
        print("final ", free)
        return len(free)
"""
[30]
[10, 30]
[10, 30]
[20, 30]

final  [20, 30]
"""
