"""
https://leetcode.com/problems/split-array-with-equal-sum/

Given an integer array nums of length n, return true if there is a triplet (i, j, k) which satisfies the following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
The sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) is equal.
A subarray (l, r) represents a slice of the original array starting from the element indexed l to the element indexed r.

Example 1:

Input: nums = [1,2,1,2,1,2,1]
Output: true
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
Example 2:

Input: nums = [1,2,1,2,1,2,1,2]
Output: false


"""


class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cumSum = []
        runSum = 0

        for i in nums:
            runSum = runSum + i
            cumSum.append(runSum)

        for j in range(3, len(nums)-3):
            track = set()

            for i in range(1, j-1):
                if cumSum[i-1] == cumSum[j-1]-cumSum[i]:
                    track.add(cumSum[i-1])

            for k in range(j+1, len(nums)-1):
                if cumSum[len(nums)-1] - cumSum[k] == cumSum[k-1] - cumSum[j] and (cumSum[k-1] - cumSum[j] in track):
                    return True

        return False


def splitArray(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    cumSum = []
    runSum = 0

    for i in nums:
        runSum = runSum + i
        cumSum.append(runSum)

    print(cumSum)
    for j in range(3, len(nums)-3):
        track = set()

        for i in range(1, j-1):
            if cumSum[i-1] == cumSum[j-1]-cumSum[i]:
                track.add(cumSum[i-1])
        print(track)
        for k in range(j+1, len(nums)-1):
            if cumSum[len(nums)-1] - cumSum[k] == cumSum[k-1] - cumSum[j] and (cumSum[k-1] - cumSum[j] in track):
                return True
                print(track)

    return False


nums = [1, 2, 1, 2, 1, 2, 1]
splitArray(nums)
