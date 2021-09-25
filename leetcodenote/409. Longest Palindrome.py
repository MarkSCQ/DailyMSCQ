"""
https://leetcode.com/problems/longest-palindrome/

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


Example 1:
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1

Example 3:
Input: s = "bb"
Output: 2
"""


"""
input: string
output: longest length that can constitude one palindrome string


"""


"""
String greedy


Solution and Idea:


This question asked to return the length of longest palindrom string that can be built using input string characters.

idea:   1 collect all data
        2 calculate the longest data

in step 2, the calculation part has several details, 
            What if the amount of current character is odd ?
            What if the amount of current character is even ? 


"""


class Solution:
    def longestPalindrome(self, s):
        data = {}

        for _item in s:
            if _item not in data:
                data[_item] = 1
            else:
                data[_item] += 1

        curr = 0
        for key in data:
            # ! we add each possible solution to the curr. //2*2 means we want to add even number. For example, if data[key]==3, then 3//2*2 will be 2.
            curr += data[key]//2*2
            # ! here is the magic, if the curernt's reminder is 0 and the current data[key] is odd, then add 1
            if curr % 2 == 0 and data[key] % 2 == 1:
                curr += 1
        # ~ when doing calculation on these two steps in the last for loop, I was wondering that what if we have many different odd characters? lets say a=3 b=7...
        # ~ at the first glance, it's not easy to find why, but if we do some analysis, we can tell that
        # ~ curr += data[key]//2*2 is actually adding the even number character to the string, which means if a=3, in this step we add aa to the result,
        # ~ the if statement below is actually doing check based on current situation whether we should accept this extra a
        # ~ in another words, curr+=data[key]//2*2 take the even part
        # ~                   if statement check whether we can append the results with extra 1
        return curr
