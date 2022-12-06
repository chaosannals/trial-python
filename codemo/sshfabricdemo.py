# fabric 这个工具好像是可以批处理多个服务器的，封装的 paramiko
# 以下示例只是连接，单连接比 paramiko 还复杂。

from fabric import Connection
from invoke import Responder
from sshconfig import *

c = Connection(
    host=SSH_HOST,
    port=22,
    user=SSH_USER,
    connect_kwargs={'password': SSH_PASS},
)
s = Responder(
    pattern=r'\[sudo\] password:',
    response=SSH_PASS,
)
r = c.run(
    'uname -s',
    hide=True,
    # watchers=[s],
)
print(r.stdout.strip())
