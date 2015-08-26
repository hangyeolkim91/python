from socket import *

svrSock = socket(AF_INET,SOCK_STREAM)
svrSock.bind(('127.0.0.1',2000))
svrSock.listen(1)
conn, addr = svrSock.accept()

recvBuf = conn.recv(1024)
print(len(recvBuf))
print(recvBuf)