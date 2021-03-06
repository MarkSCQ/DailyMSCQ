"""
1134. Armstrong Number
Given an integer n, return true if and only if it is an Armstrong number.

The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.

Example 1:

Input: n = 153
Output: true
Explanation: 153 is a 3-digit number, and 153 = 13 + 53 + 33.
Example 2:

Input: n = 123
Output: false
Explanation: 123 is a 3-digit number, and 123 != 13 + 23 + 33 = 36.
"""


class Solution:
    def isArmstrong(self, n: int) -> bool:
        sums = []
        k = 0
        ori = n
        while n > 0:
            tmp = n % 10
            n = int(n/10)

            k += 1
            sums.append(tmp)

        return True if sum([i**k for i in sums]) == ori else False
