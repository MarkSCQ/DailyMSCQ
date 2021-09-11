
# # ! input an array
while 1:
    n = int(input())
    l = list(map(int, input().split()))
    print(l)
    print(type(l))

# ! input a string and split
# while 1:
#     s = input()
#     s = s.split(" ")

# while 1:
#     # input a number
#     n = int(input())
#     print(n)
#     print(type(n))


#!/usr/bin/env python  
# coding=utf-8  
# Python使用的是3.4.3，缩进可以使用tab、4个空格或2个空格，但是只能任选其中一种，不能多种混用
while 1:
    a=[]  
    s = input()

    if s != "":
        for x in s.split():  
            a.append(int(x))  

        print(sum(a))
    else:
        break