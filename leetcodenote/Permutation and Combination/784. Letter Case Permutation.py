"""
784. Letter Case Permutation

Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. You can return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
Example 3:

Input: s = "12345"
Output: ["12345"]
Example 4:

Input: s = "0"
Output: ["0"]
"""


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [[]]

        for char in s:
            # ! get the length of current list.
            n = len(ans)
            if char.isalpha():
                # ! for each current sub list,
                # ! we first copy the origin and add at the tail
                # ! then add lower char and higher char
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n+i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)
        print(ans)
        return map("".join, ans)
