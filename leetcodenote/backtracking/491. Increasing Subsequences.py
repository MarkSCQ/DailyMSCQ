"""
https://leetcode.com/problems/increasing-subsequences/


Given an integer array nums, return all the different possible increasing subsequences of the given array with at least two elements. 
You may return the answer in any order.
The given array may contain duplicates, and two equal integers should also be considered a special case of increasing sequence.


Example 1:
Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:
Input: nums = [4,4,3,2,1]
Output: [[4,4]]

"""


def findSubsequences(nums):
    # ! resutls
    res = []

    def findsub(nums, tmplist, index):
        # ! when the tmplist size is bigger than 1 
        if len(tmplist) > 1:
            t = [tmplist[i] for i in range(len(tmplist))]
            # ! duplicate check
            if t not in res:
                res.append(t)

        # ! for each number in the nums, doing subsequence adding
        for i in range(index, len(nums)):
            # ! if the tmplist is empty or 
            # ! the last element of tmplist is smaller and equal to the current number of nums
            if len(tmplist) == 0 or tmplist[len(tmplist)-1] <= nums[i]:
                # ! append the current number to tmplist
                tmplist.append(nums[i])
                # ! continue searching for the next element
                findsub(nums, tmplist, i+1)
                # ! backtrack
                tmplist.pop(len(tmplist)-1)
        

    findsub(nums, [], 0)
    return res


nums = [4,6,7,7]
findSubsequences(nums)




# class Solution(object):

        

            
#     def findSubsequences(self, nums: List[int]) -> List[List[int]]:
#         res = []

#         def findsub(nums, tmplist, index):
#             if len(tmplist) > 1:
#                 t = [tmplist[i] for i in range(len(tmplist))]
#                 if t not in res:
#                     res.append(t)


#             for i in range(index, len(nums)):
#                 if len(tmplist) == 0 or tmplist[len(tmplist)-1] <= nums[i]:
#                     tmplist.append(nums[i])
#                     findsub(nums, tmplist, i+1)
#                     tmplist.pop(len(tmplist)-1)

#         findsub(nums, [], 0)
#         return res