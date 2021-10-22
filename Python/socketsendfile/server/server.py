import socket
import tqdm
import os


PORT = 9898
s = socket.socket()

# '' == '0.0.0.0'
s.bind(('', PORT))
s.listen(10)

file = open('recv.txt','wb')

while True:
    print(s)
    conn,addr = s.accept()
    print("IP addr ", addr[0])
    msg = f' hi client, from ip address {addr[0]}'
    conn.send(msg.encode())
    recvData = conn.recv(1024)
    while recvData:
        file.write(recvData)
        recvData = conn.recv(1024)
    file.close()
    conn.close()
    break






