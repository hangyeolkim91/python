from socketserver import ThreadingTCPServer,StreamRequestHandler

PORT = 2000

class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        conn = self.request
        print('connection from',self.client_address)
        buf = conn.recv(1024)
        if not buf:
            print('nothing')
        else:
            print(buf)

server = ThreadingTCPServer(('127.0.0.1',2000),MyRequestHandler)

print('listening on port', PORT)

server.serve_forever()




# svrSock = socket(AF_INET,SOCK_STREAM)
# svrSock.bind(('127.0.0.1',2000))
# svrSock.listen(1)
# conn, addr = svrSock.accept()
#
# recvBuf = conn.recv(1024)
# print(len(recvBuf))
# print(recvBuf)