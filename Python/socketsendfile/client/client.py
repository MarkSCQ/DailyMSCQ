import socket
import tqdm
import os


import sys

if len(sys.argv) > 1:
    serverIP = sys.argv[1]
else:
    print("Error")
    exit(1)


PORT = 9898
s = socket.socket()
s.connect((serverIP, PORT))


file=open("sample.txt",'rb')
sendData = file.read(1024)


while sendData:
    print(s.recv(1024).decode("utf-8"))
    s.send(sendData)
    sendData = file.read(1024)

s.close()