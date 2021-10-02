def findMedian(data):
    datalen = len(data)
    if datalen == 0:
        return 0
    if datalen == 1:
        return data[0]
    data.sort()

    # l = min(data)
    # r = max(data)
    # median = l+(r-l)/2

    # if median in data:
    #     print("Median")
    #     return median
    # else:
    if datalen % 2 == 0:
        print("%2")
        return (data[(datalen-1)//2]+data[(datalen-1)//2+1])/2
    else:
        print("!2")
        return data[(datalen-1)//2]


test = [
    [1],
    [1, 1],
    [1, 1, 2, 4],
    [0, 2, 5, 6, 8, 9, 9],
    [0, 0, 0, 0, 4, 4, 6, 8],
]



print(findMedian(test[0]))
print(findMedian(test[1]))
print(findMedian(test[2]))
print(findMedian(test[3]))
print(findMedian(test[4]))