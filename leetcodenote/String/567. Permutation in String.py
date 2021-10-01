"""
https://leetcode.com/problems/permutation-in-string/
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""


"""
Solution 1 sorting

Slice the stirng and compare

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        s1=sorted(s1)
        s1l = len(s1)
        for i in range(len(s2)-1):
            tmp = sorted(s2[i:i+s1l])
            if s1==tmp:
                return True 
        return False


"""
! Solution2 Sliding Window using ASCII, Hashtable-like Array(used for counting)

! using array to count the amount of characters. 

"""
class Solution2:
    def checkInclusion(self, s1, s2):
        if s1==s2:
            return True
        # ! initialize counting array, 
        # ! index->characters from ASCII ord(), 
        # ! value->the times of current character occurs
        s1list = [0 for i in range(26)]   
        s2list = [0 for i in range(26)]
        # ! initilize s1 counter  
        for i in range(len(s1)):
            s1list[ord(s1[i])-97]+=1
        
        # ! searching using sliding window
        for i in range(len(s2)):
            # ! this step, shrinking the left edge of window. 
            # ! when i is bigger then s1 length, then this means the left edge of window needs to be shift
            # ! the window size should be the same as si's length
            if i>=len(s1):
                # ! shrink the window and minus one, becuase the window is shifted
                s2list[ord(s2[i])-97]-=1                
            # ! extend the window in this round,
            # ! i is keeping increasing, the right edge of window is extending too
            s2list[ord(s2[i])-97]+=1
            # ! check whether the current window is the answer we are searching for
            if s1list==s2list:
                return True
        return False
            