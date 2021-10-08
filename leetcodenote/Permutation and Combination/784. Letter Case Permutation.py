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


"""
Move from left to right. Each time we process one element, using [] to mark the current processing element.

          [a]1b2
        /       \
    a[1]b2      A[1]b2
       |           |
    a1[b]2      a1[b]2
    /   \        /   \
a1b[2] a1B[2] A1b[2] A1B[2]

pseudocode: 
def dfs(S,i):
    if i==len(S): ans.append(S)
    dfs(S,i+1)
    if S[i] is letter:
        toggle(S[i]) # S[i]^=(1<<5)
        dfs(S,i+1)
        toggle(S[i]) # S[i]^=(1<<5)

ASCII
    Upper Case A-Z: 65-90
    Lower Case a-z: 97-122

    'a' - 'A' =32
    S[i]^=(1<<5) shift to left with 5
    
    CPP  S[i]^=(1<<5)
    
    Python S[i]= chr(ord(S[i])^(1<<5)) 
    chr(num) => string char
    chr(66) == 'B' 
    ord(S[i]) string char to number
    ^(1<<5) shift left with 5



"""


class Solution:
    def letterCasePermutation(self, s):
        res = []

        def dfs(S, index):
            # ! if index to len(s) then add to the results
            if index == len(s):
                res.append("".join(S))
                return
            # ! no matter what the next elenment is, character or number, we need move to next index
            dfs(S, index+1)
            # ! check element is number or character
            if not S[index].isalpha():
                return
            # ! change case
            S[index] = S[index].swapcase()
            dfs(S, index+1)
            # ! recover case, in this question, this step is not necessary
            S[index] = S[index].swapcase()

        dfs(list(s), 0)
        return res
