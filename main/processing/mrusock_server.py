import multiprocessing
import platform
import socket
import logging
import sys
import time
import select

LOG = logging.getLogger(__name__)

def serve(port=12345):
    global LOG
    # Windows 下需要在进程里再设置下日志，不然没有打印
    # linux 设置会导致打印双份，重复。
    # handler = logging.StreamHandler(sys.stdout)
    # formatter = logging.Formatter('[PID %(process)d] %(message)s')
    # handler.setFormatter(formatter)
    # LOG.addHandler(handler)
    # LOG.setLevel(logging.INFO)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    system_name = platform.system().lower()
    if system_name == 'windows':
        # windows 下只有一个进程可以接收。
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_EXCLUSIVEADDRUSE, 0)
    elif system_name == 'linux':
        # Linux 下会随机分配，有时多个，有时只有一个。
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    # sock.setblocking(False)
    sock.bind(('', port))
    sock.listen(1)
    LOG.info('start serve')
    while True:
        conn, addr = sock.accept()
        LOG.info(f'c: {addr}')
        while True:
            data = conn.recv(1024)
            dl = len(data)
            LOG.info(f'recv :' + data.decode('utf8'))
            if dl == 0 or data.startswith(b'quit'):
                conn.close()
                break
            else:
                conn.sendall(data)
            time.sleep(1)
    # while True:
    #     rl, wl, el = select.select([sock,], [], [], 5)
    #     for re in rl:
    #         conn, addr = re.accept()
    #         LOG.info(f'c: {addr}')
    #         while True:
    #             data = conn.recv(1024)
    #             dl = len(data)
    #             LOG.info(f'recv count: {dl}')
    #             if len(data) == 0 or data.startswith(b'quit'):
    #                 conn.close()
    #                 break
    #             else:
    #                 conn.sendall(data)
    #             time.sleep(1)


def main():
    # 设置日志。
    global LOG
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('[PID %(process)d] %(message)s')
    handler.setFormatter(formatter)
    LOG.addHandler(handler)
    LOG.setLevel(logging.INFO)

    ps = []
    for i in range(3):
        p = multiprocessing.Process(target=serve, args=(23456,))
        p.start()
        LOG.info(f'serve {i} {p.ident}')
        ps.append(p)
    for p in ps:
        p.join()

if __name__ == '__main__':
    main()
