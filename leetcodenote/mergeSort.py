def merge(arr, left, mid, right):

    leftarr = []
    rightarr = []
    n1 = mid-left+1
    n2 = right-mid
    for i in range(n1):
        leftarr.append(arr[left+i])
    for i in range(n2):
        rightarr.append(arr[i+mid+1])

    l = 0
    r = 0
    i = 0
    while l < n1 and r < n2:
        if leftarr[l] < rightarr[r]:
            arr[i] = leftarr[l]
            i += 1
            l += 1
        else:
            arr[i] = leftarr[r]
            r += 1
            l += 1
    while l<n1:
        arr[i]=leftarr[l]
        i += 1
        l += 1
    while r<n2:
        arr[i]=leftarr[l]
        i += 1
        r += 1


def mergeSort(arr, left, right):
    if right > left:
        mid = left + (right - left)//2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, mid, right)
    pass


def main():
    pass


if __name__ == '__main__':
    main()
