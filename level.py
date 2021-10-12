# import pandas as pd

# url = "https://gist.githubusercontent.com/wesleybeckner/70ae15d4143fc01d905c51011ab9c697/raw/6b6ee4ed348f00aee31b4862df8b06bc1b314692/robot_faces.csv"

# local = r"E:/Converted/robot_faces.csv"

# faces = pd.read_csv(local)

# # a = len(file[file["mouth"]=="y"].count())
# b = faces["mouth"].value_counts().to_dict()
# print(b)
# print(faces["mouth"].value_counts())

# print(faces["mouth"].value_counts()["y"])
# print(type(faces["mouth"].value_counts()))


# r1 = faces[(faces["mouth"]=="y") & (faces["nose"]=="y")]
# print(r1)


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binN = list(str(bin(N)))[2:]

    maxb = 0
    left = 0
    right = 1

    nlen = len(binN)
    print(binN)

    while left < nlen and right < nlen:

        while left < nlen and binN[left] == "1":
            left += 1
        # left = left-1
        right = left+1
        print("a ", left, right)

        while right < nlen and binN[right] == "0":
            right += 1
        maxb = max(maxb, right-left)
        print("b ", left, right)
        left = right
        right = right-1
    #     if binN[left]==1:
    #         while binN[right]!=1:
    #             right+=1
    #         maxb=max(maxb,right-left+1)
    #     left = right
    #     right = right+1
    # if binN[left]==0:
        # return 0
    print(maxb)
    if maxb and binN[-1] != 1:
        return 0
    return maxb


solution(15)
