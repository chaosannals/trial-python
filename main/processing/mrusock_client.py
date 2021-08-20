import socket
import multiprocessing

HOST = '127.0.0.1'
PORT = 23456

def call(text):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST,PORT))

    for i in range(5):
        sock.sendall(f'{i} {text}'.encode('utf8'))
        data = sock.recv(1024)
        length = len(data)
        print(f'recv {i} count: {length}')
    sock.close()

if __name__ == '__main__':
    ps = []
    for i in range(5):
        p = multiprocessing.Process(target=call, args=(f'client-{i}',))
        p.start()
        ps.append(p)
    for p in ps:
        p.join()