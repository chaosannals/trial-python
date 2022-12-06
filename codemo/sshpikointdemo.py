## paramiko 官方源码仓库 demos 文件夹有参考
# 交互

import sys
from threading import Thread
from paramiko import SSHClient
from sshconfig import *

client = SSHClient()
client.load_system_host_keys()
client.connect(
    hostname=SSH_HOST,
    port=22,
    username=SSH_USER,
    password=SSH_PASS,
)
s = client.invoke_shell()

def writeall(sock):
    while True:
        data = sock.recv(256)
        if not data:
            sys.stdout.write('EOF\n')
            sys.stdout.flush()
            break
        sys.stdout.write(str(data, encoding='utf8'))
        sys.stdout.flush()

writer = Thread(target=writeall, args=(s,))
writer.start()

try:
    while True:
        d = sys.stdin.read(1)
        if not d:
            break
        s.send(d)
except KeyboardInterrupt as e:
    pass
