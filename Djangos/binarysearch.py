def binarySearch(arr, x):
    lower = 0
    higher = len(arr)-1
    mid = 0
    exit = True
    distance = arr[-1]-arr[0]
    while(exit):

        if higher < 0 or lower > len(arr)-1 or lower > higher:
            exit = False
        mid = lower+(higher-lower)//2
        print(mid)
        if arr[mid] <= x:
            lower = mid+1
        if arr[mid] >= x:
            higher = mid-1
        if arr[mid] == x:
            exit = False

        # if arr[mid]<=x<=arr[mid+1]:
        #     exit=False

        if arr[mid] <= x < arr[mid+1]:
            exit = False

        if arr[mid] < x <= arr[mid+1]:
            mid = mid + 1
            exit = False

    print(mid)


arr = [1, 2, 2, 3, 4, 5, 6]
x = 5

binarySearch(arr, x)
