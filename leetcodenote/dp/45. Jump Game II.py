"""


Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2'

"""


class Solution:
    def jump(self, nums):
        # ! current farther distance
        currfar = 0
        # ! step counter
        step = 0

        currindex = 0
        for i in range(len(nums)-1):
            # ! i+nums[i] based on current number, the distance we can jump
            currfar = max(currfar, i+nums[i])
            # ! Step counting
            if i == currindex:
                currindex = currfar
                step += 1
        return step


def jump(nums):
    # ! current farther distance
    currfar = 0
    # ! step counter
    step = 0

    currindex = 0
    for i in range(len(nums)-1):
        # ! i+nums[i] based on current number, the distance we can jump
        currfar = max(currfar, i+nums[i])
        # ! Step counting
        if i == currindex:
            print(currindex)
            currindex = currfar
            step += 1
    return step


nums = [2, 3, 1, 1, 4]
jump(nums)
