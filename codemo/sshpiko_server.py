'''
该示例不是很友好，客户端连接后不会回显输入。
'''

from abc import ABC, abstractmethod
from cmd import Cmd
from sys import platform
from time import sleep
import os
import socket
import threading
import multiprocessing
import paramiko


HOST = '0.0.0.0'
PORT = 22

class Shell(Cmd):
    intro='Custom SSH Shell'
    use_rawinput=False
    prompt='My Shell> '

    def __init__(self, stdin=None, stdout=None):
        super().__init__(completekey='tab', stdin=stdin, stdout=stdout)

    def print(self, value):
        # make sure stdout is set and not closed
        if self.stdout and not self.stdout.closed:
            self.stdout.write(value)
            self.stdout.flush()
        
    def printline(self, value):
        self.print(value + '\r\n')

    def emptyline(self):
        self.print('\r\n')

    ## do_* 开头的提供命令
    ## 以下是2个命令 greet 和 bye

    def do_greet(self, arg):
        if arg:
            self.printline('Hey {0}! Nice to see you!'.format(arg))
        else:
            self.printline('Hello there!')

    def do_bye(self, arg):
        self.printline('See you later!')
        return True
    
    def do_EOF(self, arg):
        self.printline('[EOF]')
        return True

class ServerBase(ABC):
    def __init__(self):
        self._is_running = threading.Event()
        self._socket = None
        self.client_shell = None
        self._listen_thread = None

    def start(self, address=HOST, port=PORT, timeout=1):
        if not self._is_running.is_set():
            self._is_running.set()

            self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

            # 只有 linux 支持端口复用
            if platform == "linux" or platform == "linux2":
                self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, True)

            self._socket.settimeout(timeout)
            self._socket.bind((address, port))

            self._listen_thread = threading.Thread(target=self._listen, daemon=True)
            self._listen_thread.start()

    def stop(self):
        print("stop")
        if self._is_running.is_set():
            self._is_running.clear()
            self._listen_thread.join()
            self._socket.close()

    def _listen(self):
        while self._is_running.is_set():
            try:
                self._socket.listen()
                client, addr = self._socket.accept()
                #print('.')
                self.connection_function(client)
            except socket.timeout:
                # print('.', end='', flush=True)
                pass

    @abstractmethod
    def connection_function(self, client):
        pass


class SshServerInterface(paramiko.ServerInterface):
    def check_channel_request(self, kind, chanid):
        print(f"check_channel_request: {kind}")
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_pty_request(self, channel, term, width, height, pixelwidth, pixelheight, modes):
        print("check_channel_pty_request")
        return True

    def check_channel_shell_request(self, channel):
        print("check_channel_shell_request")
        return True
    
    def check_auth_password(self, username, password):
        print(f"login: {username}")
        if (username == "root") and (password == "123456"):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def get_banner(self):
        return ('My SSH Server\r\n', 'zh-CN')
    

def thread_work(client, host_key):
    try:
        print(f"connection_function")
        session = paramiko.Transport(client)
        # session.add_server_key(self._host_key)
        session.add_server_key(host_key)

        server = SshServerInterface()
        try:
            session.start_server(server=server)
        except paramiko.SSHException as e:
            print(f"paramiko.SSHException {e}")
            return

        # print('session.accept')
        channel = session.accept()
        stdio = channel.makefile('rwU')

        # self.client_shell = Shell(stdio, stdio)
        # self.client_shell.cmdloop()

        client_shell = Shell(stdio, stdio)
        client_shell.cmdloop()

        print('cmdloop end')

        session.close()
    except Exception as e:
        print(f"error: {e}")
        pass
class SshServer(ServerBase):
    def __init__(self, host_key_file, host_key_file_password=None):
        super(SshServer, self).__init__()
        self._host_key = paramiko.RSAKey.from_private_key_file(host_key_file, host_key_file_password)

    def connection_function(self, client):
        t = threading.Thread(target=thread_work, daemon=True, args=(client, self._host_key))
        t.start()
        print('start thread')

if __name__ == '__main__':
    home_dir = os.path.expanduser('~')
    host_key_path = os.path.join(home_dir, '.ssh', 'id_rsa')
    print(f'home: {home_dir}')
    print(f'host key: {host_key_path}')
    server = SshServer(host_key_path)
    server.start()

    try:
        while True:
            sleep(1000)
    except KeyboardInterrupt:
        print("close")
    except Exception as e:
        print(f"error: {e}")