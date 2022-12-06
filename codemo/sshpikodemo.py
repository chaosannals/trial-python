## paramiko 官方源码仓库 demos 文件夹有参考
# 交互

import sys
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
        data = sock.recv(10)
        if not data:
            sys.stdout.write('EOF\n')
            sys.stdout.flush()
            break
        sys.stdout.write(str(data, encoding='utf8'))
        sys.stdout.flush()

def command(cmd):
    s.send(f'{cmd}\n')
    d = b''
    while True:
        d += s.recv(256)
        if d.endswith(b'Password: '):
            break
        if d.endswith(b'$ '):
            break
        if d.endswith(b'# '):
            break
        # print(d)
    return str(d, encoding='utf8')

for cmd in SSH_CMDS:
    print(command(cmd))
