class Solution:
    def isValid(self, s):
        # ! construct dictionary
        dics = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        # ! for each character in the string
        for i in s:
            # ! if the element in the dic
            if i in dics:
                # ! the stack has elements
                # ! get the last element of the stack
                # ! otherwise assign ? to curr
                curr = stack[-1] if len(stack) > 0 else "?"
                # ! dics[i], when element in the dic and get its pari
                # ! if the pair of i is equal to the curr then pop the stack
                # ! else return False
                if dics[i] == curr:
                    stack.pop()
                else:
                    return False
            else:
                # ! when the element is not in the stack,
                # ! then append(push) it to the stack
                stack.append(i)
        # ! return True if stack is empty, otherwise return False
        return True if len(stack) == 0 else False
