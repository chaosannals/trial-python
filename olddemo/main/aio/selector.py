import selectors
import socket
import struct

class TcpServer:
    def __init__(self, host, port):
        self.socket = socket.socket()
        self.socket.bind((host, port))
        self.socket.listen(100)
        self.socket.setblocking(False)
        self.selector = selectors.DefaultSelector()

        def read(conn, mask):
            try:
                data = conn.recv(1000)
                if data:
                    r = struct.unpack('>HIH', data)
                    print("{}".format(r))
                    p = struct.pack('>HIH', r[2], r[1], r[0])
                    conn.send(p)
                else:
                    self.selector.unregister(conn)
                    conn.close()
            except BaseException as e:
                self.selector.unregister(conn)
                conn.close()
                print(e)

        def accept(sock, mask):
            conn, addr = sock.accept()
            conn.setblocking(False)
            self.selector.register(conn, selectors.EVENT_READ, read)

        self.selector.register(self.socket, selectors.EVENT_READ, accept)

    def listen(self):
        while True:
            events = self.selector.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)

server = TcpServer('localhost', 8000)
server.listen()