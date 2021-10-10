import pandas as pd

url = "https://gist.githubusercontent.com/wesleybeckner/70ae15d4143fc01d905c51011ab9c697/raw/6b6ee4ed348f00aee31b4862df8b06bc1b314692/robot_faces.csv"

local = r"E:/Converted/robot_faces.csv"

faces = pd.read_csv(local)

# a = len(file[file["mouth"]=="y"].count())
b = faces["mouth"].value_counts().to_dict()
print(b)
print(faces["mouth"].value_counts())

print(faces["mouth"].value_counts()["y"])
print(type(faces["mouth"].value_counts()))


r1 = faces[(faces["mouth"]=="y") & (faces["nose"]=="y")]
print(r1)