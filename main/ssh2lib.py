import socket
from io import BytesIO
from ssh2.session import Session


def ssh2_open(host, port=22, user='root', keyfile='opskey'):
    '''
    
    '''

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    session = Session()
    session.handshake(sock)
    session.userauth_publickey_fromfile(user, keyfile)
    return session

def ssh2_exec(session, cmd):
    '''
    
    '''
    channel = session.open_session()
    channel.execute(cmd)
    size, data = channel.read()
    buff = BytesIO()
    while size > 0:
        buff.write(data)
        size, data = channel.read()
    channel.close()
    c = channel.get_exit_status()
    return buff.getvalue(), c

if __name__ == '__main__':
    s = ssh2_open('127.0.0.1')
    b, c = ssh2_exec(s, 'cd /root; pwd')
    print(str(b, encoding='utf8'), c)