"""
https://leetcode.com/problems/shortest-word-distance/


Share
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, 
return the shortest distance between these two words in the list.


Example 1:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

Example 2:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1

"""

# ! NOTICE: need to avoid the initialization case!!! 
# ! if index1!=len(wordsDict) and index2!=len(wordsDict):
# !     mindis = min(mindis,abs(index2-index1))

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index1 = len(wordsDict)
        index2 = len(wordsDict)
        
        mindis = len(wordsDict)-1
        for i in range(len(wordsDict)):
            if wordsDict[i]==word1:
                index1=i
            if wordsDict[i]==word2:
                index2=i
            if index1!=len(wordsDict) and index2!=len(wordsDict):
                mindis = min(mindis,abs(index2-index1))
        return mindis
                
        
