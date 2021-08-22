


import seaborn as sns
import pandas as pd

def hello():
    print("hi")

sns.plot()









hello()








"""


infos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

extracts = [2, 4, 6, 8, 10]


def extractNums(infos, extracts):
    # ! 1 exchanging nums
    head_idx = 0
    tail_idx = len(infos)-1

    while head_idx < tail_idx:
        if infos[head_idx] not in extracts and infos[tail_idx] not in extracts:
            head_idx += 1
        elif infos[head_idx] not in extracts and infos[tail_idx] in extracts:
            tail_idx -= 1
        elif infos[head_idx] in extracts and infos[tail_idx] not in extracts:
            tmp = infos[head_idx]
            infos[head_idx] = infos[tail_idx]
            infos[tail_idx] = tmp
            head_idx += 1
            tail_idx -= 1
        elif infos[head_idx] in extracts and infos[tail_idx] in extracts:
            tail_idx -= 1
        else:
            print(infos)

    print(infos)

    # ! sort and reassign
    infos = sorted(infos[:len(infos)-len(extracts)]) + \
        sorted(infos[len(infos)-len(extracts):])
    print(infos)

    # O(n+nlogn)


extractNums(infos, extracts)
"""