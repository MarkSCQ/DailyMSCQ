"""
https://leetcode.com/problems/subarray-sum-equals-k/
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

"""

# ! cannot apply naive double iteration method in python, timeout

# ~ HashMap and Array 
# ~ two different implementation of python using dictionary
# ~ the main difference is the get() function

# ! Return Value from get()
# ! get() method returns:
# ! the value for the specified key if key is in the dictionary.
# ! None if the key is not found and value is not specified.
# ! value if the key is not found and value is specified.

# ! if the key not in the dictionary and the value is specified, get(key,value) will return value
# ! if the key is in the dictionary and the value is specified but different from the value in the dictionary, 
# !     then it will return the value in the dictionary instead of the value specified in the get function


"""
solution: using cumulative sum and hashmap(dictionary)

1 store the cumulative sum in the dictionary
    the key is the cumulative sum value;
    the value is the frequency that this sum exists in the previous calculations
2 each time check whether the data is in the dictionary or not
    target is the k value, using [tmp-k in culsum] will check whether the key exists
        if exist count+culsum[tmp-k] add the previous frequency
    if tmp exists in culsum, the tmp frequency +1
    else set as 1

"""


class Solution:
    def subarraySum(self, nums, k):
        culsum = {0: 1}
        count = 0
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            if tmp-k in culsum:
                count += culsum[tmp-k]
            else:
                count += 0
            if tmp in culsum:
                culsum[tmp] += 1
            else:
                culsum[tmp] = 1
        return count

    # def subarraySum(self, nums, k):
    #     count, cur, res = {0: 1}, 0, 0
    #     for v in nums:
    #         cur += v
    #         res += count.get(cur - k, 0)
    #         count[cur] = count.get(cur, 0) + 1
    #     return res
