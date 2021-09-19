"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""


def topKFrequent(self, nums, k):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 0
    for nm in nums:
        dic[nm] += 1
    dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    li = []
    for key in dic:
        if k > 0:
            li.append(key)
            k -= 1
        else:
            break
    return li
