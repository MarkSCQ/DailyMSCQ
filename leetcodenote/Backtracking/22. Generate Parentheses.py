"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""


# ! NOTICE:
# !     1. the total amount of symbols within a pair is 2*n,
# !        which means if a pair reach 2*n size, it has been done
# !


"""
( open
) close

only add open paranthesis if open < n
only add a closing paranthesis if close <open
valid IIF open == close == n
"""


class solution:
    def solve(self, n):
        stack = []  # hold paranthesis
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN+1)
                stack.pop()
        backtrack(0,0)
        return res

class Solution2:
    def generateParenthesis(self, n):
        ans = []

        def backtrack(S=[], left=0, right=0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans


class Solution3(object):
    def generateParenthesis(self, N):
        if N == 0:
            return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans


class Solution1(object):
    def generateParenthesis(self, n):
        # ! A is used to wrap the ()s
        def generate(A=[]):
            # ! if the size of A is 2 times of input number n, then put A in to result list.
            # ! valid(A) check if one pair is validly closed
            if len(A) == 2*n:
                if valid(A):
                    # ! add valid pair to result ans list
                    ans.append("".join(A))
            else:

                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        # ! check if one pair is valid
        def valid(A):
            bal = 0
            # ! balance number is 0. ( +1   ) -1
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        ans = []
        generate()
        return ans
