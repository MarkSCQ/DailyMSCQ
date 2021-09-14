# def findPrimeNumber(num):
#     pnums = []

#     i = 2
#     nlim = int(num**0.5+1)
#     while num != 1:
#         if num % i == 0:
#             pnums.append(i)
#             num = num//i

#         else:
#             if num > nlim:
#                 pnums.append(num)
#                 break
#             else:
#                 i += 1
#     for i in pnums:
#         print(i, end=" ")


# while True:
#     nun = int(input())
#     findPrimeNumber(num)
while True:
    try:
        n, curNum = int(input()), 1  
        res = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(i + 1):
                res[i - j][j] = curNum
                curNum += 1
        print(res)
        for i in res:
            print(" ".join(map(str, (filter(lambda i: i != 0, i)))))
    except:
        break