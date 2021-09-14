def isPerfect(n):
    fplist = []
    limit = int(n/2+1)
    for i in range(1,limit):
        if n%i==0:
            fplist.append(i)

    return sum(fplist)==n

while True:
    
    try:
        n = int(input())
        count = 0

        for i in range(1,n):
            if isPerfect(i):

                count+=1
        print(count)
    except e:
        print(e)