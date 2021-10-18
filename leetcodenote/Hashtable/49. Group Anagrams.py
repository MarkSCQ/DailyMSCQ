"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 


"""


class Solution:
    def groupAnagrams(self, strs):
        dic = {}

        def constructdic(word):
            l = [0 for i in range(26)]
            for i in list(word):
                l[ord(i)-97] += 1
            return tuple(l)

        for word in strs:

            t = constructdic(word)
            if t not in dic:
                dic[t] = [word]
            else:
                dic[t].append(word)

        res = []
        for i in dic:
            res.append(dic[i])
        return res


class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        res = defaultdict(list)

        for word in strs:
            count = [0]*26

            for i in word:
                count[ord(i)-ord("a")] += 1

            res[tuple(count)].append(word)

        return res.values()
