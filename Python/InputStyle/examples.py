# input two numbers
def inputStyle1():
    while True:

        try:
            a, b = map(int, input().strip().split())
        except:
            break
        print(a, b)


# input one list
def inputStyle2():
    while True:
        try:
            l = list(map(int, input().strip().split()))
            print(l)
        except:
            break


# input one matrix
def inputStyle3():
    while True:
        matrix = []
        width = 0
        height = 0
        try:
            height, width = map(int, input().strip().split())
            for i in range(height):
                l = list(map(int, input().strip().split()))
                matrix.append(l[:width])
            print(matrix)
        except:
            break


# input different lists in one trial
def inputStyle4():
    while True:
        amount = int(input())
        data = []

        try:
            for i in range(amount):
                data.append(list(input().strip().split()))
            print(data)
        except:
            break


inputStyle4()
