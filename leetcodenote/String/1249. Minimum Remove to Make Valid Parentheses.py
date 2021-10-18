"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
     
"""

"""
Core: stack, though we do not really apply stack in this problem

"""


class Solution:
    def minRemoveToMakeValid(self, s):

        sl = list(s)
        sb = []

        # ! the opened is the unbalanced factor
        # ! when opened>0 the amount of ( is greater than amount of )
        # ! when opened<0 the amount of ( is smaller than amount of )
        # ! when opened==0 the amount of ( is equal to amount of )
        opened = 0

        # ! iterating the string, count the amount of unbalanced brackets
        # ! if 0, then we skip the current ), because add it to sb tmp will cause unbalance
        for i in range(len(sl)):
            # ! ( +1      ) -1
            # ! if current element is (, then we add current elements to the sb temp. (positive opened, we have extra ()
            if sl[i] == "(":
                opened += 1
            elif sl[i] == ")":
                if opened == 0:
                    # ! if 0, then we skip the current ), because add it to sb tmp will cause unbalance
                    # ! we need to skip the current ) by using continue statement
                    # ! if opened is greater than 0, then we can adapt more )
                    continue
                opened -= 1
            # ! add string elements to the tmp list,
            # ! this sb list will only add
            # ! 1. (
            # ! 2. ) when open is greater than 0, which means the unbalance is caused by (
            # ! 3. Normal, non-bracket characters
            sb.append(sl[i])

        # ! after the first for iteration, the amount of ) is smaller or equal to (
        # ! the second iteration, it will filter out the unbalanced (
        res = []
        # ! iterate the tmp sb list from tail
        for i in range(len(sb)-1, -1, -1):
            # ! remove the unbalance caused by extra (
            if sb[i] == "(" and opened > 0:
                opened -= 1
                continue
            res.append(sb[i])
        res.reverse()
        # ! reverse the results and make it string
        return "".join(res)
