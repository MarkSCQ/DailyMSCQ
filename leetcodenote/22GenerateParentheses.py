
# ! NOTICE:
# !     1. the total amount of symbols within a pair is 2*n,
# !        which means if a pair reach 2*n size, it has been done
# !     2. 
# !
# !



'''
Solution 1 Recursion

'''
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
