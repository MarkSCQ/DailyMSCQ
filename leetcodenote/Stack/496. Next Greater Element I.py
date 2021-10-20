"""
https://leetcode.com/problems/next-greater-element-i/

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.


"""


"""
stack approach 

dictionary: 
    key: element from the frist for iteration and the second while iteration(more preciously, from the stack) 
    value: next greater element

stack is used to store the number
for each number, if it is smaller than the stack top element, then put it in to the dictionary


"""


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # ! function as middle tool
        stack = []
        dic = {}
        for i in range(len(nums2)):
            # ! for each number,
            # ! if stack is not empty and number in the stack is smaller than the one in nums2
            # ! add it to the dictionary
            while stack and nums2[i] > stack[-1]:
                dic[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        # ! for the values that we fail to find the next greater, we assign them with -1
        while stack:
            dic[stack.pop()] = -1

        res = []

        for i in nums1:
            res.append(dic[i])

        return res
