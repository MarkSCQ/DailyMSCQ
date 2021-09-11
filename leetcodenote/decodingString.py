class Solution:
    # ~ https://leetcode.com/problems/decode-string/ 
    # ! the sturcture must follow k[.....]
    def decodeString(self, s: str) -> str:
        # ! stack to store temp string
        stack = [] 
        # ! iterate the string
        for i in range(len(s)):
            # ! when read  ], which denotes there existing one closed []
            # ! put the content of the closed [] into the stack
            if s[i] == ']':
                ds = []
                # ! ds is used to store the temp char elements
                while stack[-1] != '[':
                    ds.append(stack.pop())
                stack.pop()
                base = 1
                k = 0
                # ! Extract the number, isdigit(): is current str a number?
                while len(stack) != 0 and stack[-1].isdigit():
                    k = k+int(stack.pop())*base
                    base *= 10
                # ! inner put ds contents to stack
                # ! outer repeat K times
                while k != 0:
                    nestidx = len(ds)-1
                    while nestidx >= 0:
                        stack.append(ds[nestidx])
                        nestidx -= 1
                    k -= 1
            else:
                # ! if string is not closed with ] then continue add them in
                stack.append(s[i])

        # ! prefill the results array with empty values
        result = ["" for i in range(len(stack))]
        lidx = len(result)-1
        # ! assign stack(list) values to results list
        while lidx >= 0:
            result[lidx] = stack.pop()
            lidx -= 1

        return "".join(result)
