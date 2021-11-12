
def f1(s):
    dic = {}
    slist = list(s)
    left = 0
    right = 0
    strlen = len(s)
    maxlen = 0
    while right < strlen:

        if slist[right] not in dic:
            dic[slist[right]] = 1
        else:
            dic[slist[right]] += 1

        while dic[slist[right]] > 1:
            left += 1
            dic[slist[right]] -= 1
        maxlen = max(maxlen, right - left+1)
        right += 1
    return maxlen


def f1(s):
    dic = {}
    maxlen = 0
    left = right = 0

    strlen = len(s)
    slist = list(s)

    while right < strlen:
        dic[slist[right]] = right

        while dic[slist[right]] >= 3:

            leftToDelete = min(dic.values)

            del dic[slist[leftToDelete]]
            left += 1
        maxlen = max(maxlen, right-left)
    return right


def f2(arr, target):
    left = right = 0

    minlen = len(arr)
    sm = 0
    while right < len(arr):

        sm += arr[right]
        while sm >= target:
            minlen = min(minlen, right-left+1)
            sm -= arr[left]
            left += 1

        right += 1


def gp(n):
    stack = []
    res = []

    def backtracking(openN, closeN):
        if openN == closeN:
            res.append("".join(stack))
            return
        if closeN < openN:
            stack.append(")")
            backtracking(openN, closeN+1)
            stack.pop(")")

        if openN < n:
            stack.append("(")
            backtracking(openN+1, closeN)
            stack.pop("(")
    backtracking(0, 0)
    return res


def perm(nums):

    res = []
    if len(nums) ==1:
        return [nums[:]]

    for i in range(len(nums)):

        num = nums.pop(0)

        p = perm(nums)
        for j in range(len(p)):
            p[j].append(num)
        res.extend(p)
        nums.append(num)

    return res


def comb(n,k):


    res = []
    def backtracking(first=1,curr=[]):
        if len(curr) == k:
            res.append(curr)

        for i in range(first,n+1):
            curr.append(i)
            backtracking(i+1,curr)
            curr.pop()
    backtracking()
    return res