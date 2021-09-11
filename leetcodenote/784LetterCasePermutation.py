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
