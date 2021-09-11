# def res(n):
#     num1 = 1
#     num2 = 2
#     num3 = 3
#     num4 = 0
#     if n == 1:
#         return num1
#     if n == 2:
#         return num2
#     if n == 3:
#         return num3

#     for i in range(4, n+1):
#         num4 = num2+num3
#         num2 = num3
#         num3 = num4
#     print(num4)
#     return num4


# while 1:
#     nm = int(input())
#     N = nm
#     b = res(N)
#     print(b)

# def test1(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n == 3:
#         return 3
#     return test1(n-2)+test1(n-1)


# def test():
#     import sys
#     for a in sys.stdin:
#         b = int((a.split())[0])
#         print(b)
# test()
# def count(m):
#     if m <= 3:
#         return m-1
#     else:
#         return count(m-1)+count(m-2)


# n = int(input())
# print("n: ", n)
# for i in range(n):
#     m = int(input())
#     c = count(m)
#     print(c)
'''


def value(n):
    x=3
    i=3
    j=1
    out=0
    while x<=n:
        if n<x+i:
            out=n-2*j
            break
        else:
            x+=i
            i+=1
            j+=1
    return out
while 1:
    try:
        n=int(input())
        if n<=2:
            print(n)
        else:
            print(value(n))
    except:
        break
    n = int(input())

for i in range(n):
    lent = int(input())
    listx = [x+1 for x in range(lent)]
    while 1:
        if len(listx)>3:
            for x1 in range(int(len(listx)/2)):
                listx.pop(x1+1)
        else:
            break
        if len(listx)>3:
            for x2 in range(int(len(listx)/3)):
                listx.pop(2*x2+2)
        else:
            break
    for ii in listx:
        print(ii,end = ' ')
    print()
    '''


# def removeKids(kids):
#     # print("original: ", kids)
#     while len(kids) > 3:
#         # ~ remove 2nd
#         # print(kids)
#         for i in range(len(kids)//2):
#             kids.pop(i+1)
#         # print("after 2nd: ", kids)
#         if len(kids) <= 3:
#             break
#         # ~ remove 3rd
#         for i in range(len(kids)//3):
#             kids.pop(2*i+2)
#         # print("after 3rd: ", kids)
#         if len(kids) <= 3:
#             break
#     print(kids)

# kids1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# kids2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# kids3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#          21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
# removeKids(kids3)


# def removeKids(kids):
#     while len(kids)>3:
#         for i in range(len(kids)/2):
#             kids.pop(i+1)
#         if len(kids)<=3:
#             break
#         for i in range(len(kids)/3):
#             kids.pop(2*i+2)
#         if len(kids)<=3:
#             break
#     if len(kids)>2:
#         print(kids)

# def test():
#     import sys
#     for a in sys.stdin:
#         b = int((a.split())[0])
#         print(b)
#         kids=[i+1 for i in range(b)]
#         removeKids(kids)

# test()

# n = int(input())

# for i in range(n):
#     lent = int(input())
#     listx = [x+1 for x in range(lent)]
#     while 1:
#         if len(listx) > 3:
#             for x1 in range(int(len(listx)/2)):
#                 listx.pop(x1+1)
#         else:
#             break
#         if len(listx) > 3:
#             for x2 in range(int(len(listx)/3)):
#                 listx.pop(2*x2+2)
#         else:
#             break
#     for ii in listx:
#         print(ii, end=' ')
#     print()


def removeKids(kids):
    while len(kids) > 3:
        for i in range(len(kids)//2):
            kids.pop(i+1)
        if len(kids) <= 3:
            break
        for i in range(len(kids)//3):
            kids.pop(2*i+2)
        if len(kids) <= 3:
            break
    for ii in kids:
        print(ii, end=' ')
    print()


def test():
    n = int(input())
    for a in range(n):
        b = int(input())
        kids = [i+1 for i in range(b)]
        removeKids(kids)

# test()

# def reverseWords(words):
#     words = words.split(" ")
#     words.reverse()
#     return " ".join(words)

# words = "hello xiao mi"

# w = reverseWords(words)
# print(w)

# while 1:
#     s = input()
#     s = s.split(" ")
#     s = s[::-1]
#     print(" ".join(s))


while 1:
    n = int(input())
    ta = input().split()
    l = list(map(int, ta))
    print("ta: ", type(ta))
    print("l: ", l)
    j = sorted(l)
    # ! input l and j, different element index,
    # ! [2,3] means elements at index 2 and index 3, the elements are different
    o = [i for i in range(n) if l[i] != j[i]]
    print("o: ", o)
    # ! set the first differnet and the last different element index as start and end
    # ! this means the REVERSE will be put on this range
    start, end = o[0], o[-1]
    print(start, " ", end)
    # ! c is the reversed numbers from original input
    c = l[start:end+1]
    print("c: ", c)
    # ! if  l[:start] the original input from head to start +
    # !     c[::-1]   the potential reversed list +
    # !     l[end+1:] the rest original input
    # !     is the same as sorted original input, then yes
    # ! else no
    if l[:start]+c[::-1]+l[end+1:] == j:
        print("yes")
    else:
        print("no")
