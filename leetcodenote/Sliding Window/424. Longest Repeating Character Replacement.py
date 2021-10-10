"""
https://leetcode.com/problems/longest-repeating-character-replacement/


You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

"""


class Solution:
    def characterReplacement(self, s, k):
        # ! we only have 26 upper case characters, this array is used as frequency counting
        counter = [0 for i in range(26)]

        left = 0
        right = 0
        strlen = len(s)
        res = 0
        maxcount = 0

        while right < strlen:
            # ! counter+1 when taking one element
            counter[ord(s[right])-65] += 1
            # ! caluculate the current max count
            maxcount = max(maxcount, counter[ord(s[right])-65])
            # ! right index move
            right += 1

            # ! when to move? the current max amount+ k is less then the window size.
            # ! max count is the max number of repeated numbers, k is the number of characters that we can process
            if right-left > maxcount+k:
                # ! left window is going to move ahead, recover left
                counter[ord(s[left])-65] -= 1
                # ! left index move
                left += 1
            # ! update results
            res = max(res, right-left)
        return res



# ! another version of placing left and right index increaments statement
class Solution:
    def characterReplacement(self, s , k ):
        
        counter = [0 for i in range(26)]
        
        left = 0
        right = 0
        strlen = len(s)
        res = 0
        maxcount=0
        
        while right<strlen:
            
            counter[ord(s[right])-65]+=1
            maxcount = max(maxcount,counter[ord(s[right])-65])
            
            if right-left+1>maxcount+k:
                counter[ord(s[left])-65]-=1
                left+=1
            
            right+=1
            res = max(res,right-left)
        return res

