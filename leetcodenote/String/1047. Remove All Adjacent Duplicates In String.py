def removeDuplicates(S):
    output = []
    for ch in S:
        if output and ch == output[-1]:
            output.pop()
        else:
            output.append(ch)
    return ''.join(output)


def removeDuplicates2(a):
    s = []
    # 前一个被消除的元素
    del_str = ''
    for i in a:
        # 栈为空，直接添加入栈
        if len(s) == 0:
            if del_str == '':
                # 判断是首次添加，无消除字符
                s.append(i)
            else:
                # 如果不是首次，列表被删空了
                if i == del_str:
                    # 如果相等不做处理
                    continue
                else:
                    s.append(i)
                    del_str = ''  # 还原del_str
        else:
            # 判断i 与被前一个被消除的元素是都相等
            if i == del_str:
                # 如果相等不做处理
                continue
            # 判断 i 与栈顶元素是否相等
            elif i == s[-1]:
                # 弹出栈顶元素
                del_str = s.pop()
            else:
                # 入栈
                s.append(i)
                del_str = ''  # 还原del_str
    print("".join(s))


# a = "abcccbxezzzrf7788fn" 得到 "axern"
# a = "abcccdcececfc" 得到 "abdcececfc"
# a = "1jj11j1" 得到 "j1"
removeDuplicates2("1jj11j1")


def myRemoveDuplicates(string):
    lastDel = ""
    stack = []

    for char in string:
        if len(stack) == 0:
            if lastDel == "":
                stack.append(char)
            else:
                if lastDel == char:
                    continue
                else:
                    stack.append(char)
                    lastDel = ""
        else:
            if char == lastDel:
                continue
            elif char == stack[-1]:
                lastDel = stack.pop()
            else:
                stack.append(char)
                lastDel = ""
        
    return "".join(stack)


print(myRemoveDuplicates("1jj11j1"))
