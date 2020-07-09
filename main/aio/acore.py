import asyncore

class TcpHandler(asyncore.dispatcher_with_send):
    def handle_read(self):
        data = self.recv(8192)
        if data:
            self.send(data)

class TcpServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accepted(self, sock, addr):
        TcpHandler(sock)

server = TcpServer('localhost', 8080)

# 全局的，定义的类，继承分发器构造时自动注册。
asyncore.loop()
