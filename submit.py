import os


def submit_default():

    cmd_list = ["git pull",
                "git add .",
                "git commit -m ''",
                "git push"]

    for i in cmd_list:
        os.system(i)


def SubmiMain():
    print("1. Default Submit")

    print("2. Update Default Submit")

    print("3. Config Settings")

    exit = False

    while not exit:
        pass


print("Select:")
print("1. Submit")
print("2. Config My Github Account")
submit_default()
