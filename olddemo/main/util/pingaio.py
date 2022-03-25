import asyncio
import socket
import struct
import select
import time
from ipaddress import ip_network

class ICMPRequest:
    '''
    请求
    '''

    def __init__(self, loop):
        '''

        '''

        self.loop = loop
        self.data_type = 8 # ICMP Echo Request
        self.data_code = 0 # 必须为0
        self.data_checksum = 0 #
        self.data_id = 0 #
        self.payload = b'0123456789AaBbCcDdEeFfGgHhIiJjKk' # 32字节的负载数据

    async def ping(self, target_ip):
        '''
        '''
        
        print('ping {}...'.format(target_ip))
        for i in range(0, 4):
            sequence = i + 1
            packet = self.pack(sequence)
            times = await self.send(packet, target_ip, sequence)
            if times > 0:
                print('{}: 字节=32 时间={}ms'.format(target_ip, int(times * 1000)))
                await asyncio.sleep(0.7)
            else:
                print("请求超时。")

    async def send(self, packet, ip, sequence, timeout=2):
        '''
        '''
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_RAW,
            socket.getprotobyname("icmp")
        )
        start_time = time.time()
        sock.sendto(packet, (ip, 80))
        
        while True:
            start_select_time = time.time()
            what_ready = select.select([sock], [], [], timeout)
            wait_for_time = time.time() - start_select_time
            if what_ready[0] == []:
                return -1
            start_receive_time = time.time()
            receive_packet, _ = sock.recvfrom(1024)
            header = receive_packet[20:28]
            r_type, _, _, _, r_sequence = struct.unpack(
                '>BBHHH', header
            )
            if r_type == 0 and r_sequence == sequence:
                return start_receive_time - start_time

            if timeout <= wait_for_time:
                return -1

    def pack(self, sequence):
        '''
        '''
        packet = struct.pack(
            '>BBHHH32s',
            self.data_type,
            self.data_code,
            self.data_checksum,
            self.data_id,
            sequence,
            self.payload
        )
        checksum = self.check(packet)
        return struct.pack(
            '>BBHHH32s',
            self.data_type,
            self.data_code,
            checksum,
            self.data_id,
            sequence,
            self.payload
        )

    def check(self, data):
        '''
        '''
        n = len(data)
        m = n % 2
        s = 0
        for i in range(0, n - m, 2):
            s += data[i] + (data[i+1] << 8)
        if m:
            s += data[-1]
        s = (s >> 16) + (s & 0xffff)
        s += s >> 16
        result = ~s & 0xffff
        return result >> 8 | (result << 8 & 0xff00)


class Pinger:
    def __init__(self, count):
        self.count = count

    def __aiter__(self):
        return self
    
    async def __anext__(self):
        self.count -= 1
        if self.count <= 0:
            raise StopAsyncIteration
        request = ICMPRequest(loop)
        await request.ping('www.baidu.com')
        return self.count

async def main(loop):
    '''
    程序主循环
    '''

    tasks = []
    for ip in ip_network('192.168.0.0/24'):
        request = ICMPRequest(loop)
        task = request.ping(f'{ip}')
        tasks.append(task)
    dones, pendings = await asyncio.wait(tasks)
    print(dones, pendings)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()