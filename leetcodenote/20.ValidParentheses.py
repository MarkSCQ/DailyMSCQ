class Solution:
    def isValid(self, s):
        dics = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for i in s:
            if i in dics:
                curr = stack[-1] if len(stack) > 0 else "?"
                if dics[i] == curr:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if len(stack) == 0 else False
