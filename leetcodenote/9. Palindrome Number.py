"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false
"""



class Solution:
    def isPalindrome(self, x):
        
        if not (0 <= x <= 2147483647):
            return False
        # ! Revert half of the number
        # ! store the first half in store_num
        store_num = []
        while x > 0:
            t = x % 10
            store_num.append(t)
            x = int(x / 10)
        returnFlag = True
        # ! compare the store_num with the second half of the array
        for i in range(int(len(store_num)/2)):
            if store_num[i] != store_num[len(store_num)-1 - i]:
                returnFlag = False
                return returnFlag
        return True
