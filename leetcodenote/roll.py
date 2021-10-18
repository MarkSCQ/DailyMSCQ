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

    files_list = []
    for key in files:
        for f in files[key]:
            files_list.append([key, f])

    df = pd.DataFrame(files_list, columns=['type', 'question'], dtype=float)
    df.to_csv("allques.csv", mode=default)


def RollToday(default=3):
    pathFromQues = "../leetcodenote/allques.csv"
    pathFromRecords = "../leetcodenote/record.csv"

    quesAll = pd.read_csv(pathFromQues)["question"].to_list()
    quesRec = pd.read_csv(pathFromRecords)["question"].to_list()

    notFinised = True

    today = []
    while notFinised:
        if len(today) == default:
            notFinised = False
            break

        quesIndex = np.random.randint(0, len(quesAll)-1)
        toAddQues = quesAll[quesIndex]
        if toAddQues not in quesRec:
            today.append(toAddQues)
            # quesRec.add(toAddQues)

    quesDf = pd.read_csv(pathFromQues)

    # ! update rec
    for i in today:
        _type = quesDf.loc[quesDf.question == i, "type"].values[0]
        # print(_type)
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
RollToday(default=3)
