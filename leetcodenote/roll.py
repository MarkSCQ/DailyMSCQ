import os
import pandas as pd
import numpy as np

from datetime import date


def readFilesToCsv(default='a'):
    path = r"../leetcodenote/"
    folders = os.listdir(path)

    files = {}
    for fold in folders:
        if fold != "imgs":
            fp = os.path.join(path, fold)

        if os.path.isdir(fp):
            files[fold] = os.listdir(fp)
    files_dic = {}
    files_list = []

    for key in files:
        files_dic[key] = []
        for f in files[key]:
            checkf = f.split('.')
            if checkf[-1] == "md" or checkf[-1] == "png":
                continue

            files_dic[key].append(f)
        files_dic[key] = sorted(
            files_dic[key], key=lambda x: int(x.partition('.')[0]))
        print(files_dic[key])
    for key in files_dic:
        for f in files_dic[key]:
            files_list.append([key, f])
    df = pd.DataFrame(files_list, columns=['type', 'question'], dtype=float)
    df.sort_values(by=['type'])
    df.to_csv("allques.csv", mode=default)


def RollToday(default=3):
    pathFromQues = "../leetcodenote/allques.csv"
    pathFromRecords = "../leetcodenote/record.csv"

    quesAll = pd.read_csv(pathFromQues)["question"].to_list()
    quesRec = pd.read_csv(pathFromRecords)["question"].to_list()

    notFinised = True

    today = set()
    while notFinised:
        if len(today) == default:
            notFinised = False
            break

        quesIndex = np.random.randint(0, len(quesAll)-1)
        toAddQues = quesAll[quesIndex]
        if toAddQues not in quesRec:
            today.add(toAddQues)

    quesDf = pd.read_csv(pathFromQues)

    # ! update rec
    for i in today:
        _type = quesDf.loc[quesDf.question == i, "type"].values[0]
        todayques = {
            "date": [str(date.today())],
            "type": [_type],
            "question": [i],
        }
        todaydf = pd.DataFrame(todayques)
        todaydf.to_csv(
            "../leetcodenote/record.csv",
            mode='a', index=False, header=False)


# readFilesToCsv('w')
RollToday(default=4)
