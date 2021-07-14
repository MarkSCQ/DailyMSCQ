import os


def submit_default():

    cmd_list = ["git pull", "git add .", "git commit -m 'msg'", "git push"]

    for i in cmd_list:
        os.system(i)

def SubmiMain():
    pass
print("1. Default Submit")
print("2. New Submit")



print("Select:")
print("1. Submit")
print("2. Config My Github Account")
submit_default()