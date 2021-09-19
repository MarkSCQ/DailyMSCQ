"""
7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

```
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0

Constraints:

-231 <= x <= 231 - 1"""


class Solution:
    def reverse(self, x):
        pn = 1 if x >= 0 else -1
        x = abs(x)
        st = []
        while x > 0:
            t = x % 10
            st.append(t)
            x = (x-t)/10
        nm = int(sum([st[i]*10**(len(st)-i-1) for i in range(len(st))]))*pn
        if (-1)*2**31 <= nm <= 2**31-1:
            return nm
        else:
            return 0
