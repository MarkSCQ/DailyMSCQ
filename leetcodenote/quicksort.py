def partition(left, right, arr):
    pivot_index = left
    pivot = arr[pivot_index]
    # ! set initialized pivot by using "left"
    while left < right:
        while left < len(arr) and arr[left] <= pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
        print(arr)
        print("pivot index: ", pivot_index, "   pivot ele: ", pivot)
        print("left: ", left, "   right: ", right)
    print("right: ", right, "   right ele:", arr[right])
    print("pivot_index: ", pivot_index,
          "   pivot_index ele:", arr[pivot_index])

    arr[right], arr[pivot_index] = arr[pivot_index], arr[right]

    return right


def partition2(left, right, arr):
    pivot = arr[right]

    i = left-1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1


def qSort(left, right, arr):
    if left < right:
        p = partition2(left, right, arr)
        print("p :", p)
        qSort(left, p-1, arr)
        qSort(p+1, right, arr)
    return arr


def changearr(arr):
    arr[0] = 1000000


test = [3, 2, 1, 5, 4, 6]
# print(qSort(0, len(test)-1, test[:]))

t = qSort(0, len(test)-1, test[:])
print(t)
print(test)


changearr(test)
print(test)
