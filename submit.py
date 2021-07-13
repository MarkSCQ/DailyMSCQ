import os


cmd_list=["git pull","git add .","git commit -m 'msg'", "git push"]

for i in cmd_list:
    os.system(i)