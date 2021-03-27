import asyncio
import socket
import struct
import select
import time
from ipaddress import ip_network

class Packer:
    '''
    '''

    data_type = 8 # ICMP Echo Request
    data_code = 0 # 必须为0
    data_checksum = 0 #
    data_id = 0 #
    payload = b'0123456789AaBbCcDdEeFfGgHhIiJjKk' # 32字节的负载数据

    @classmethod
    def pack(cls, sequence):
        '''
        '''

        packet = struct.pack(
            '>BBHHH32s',
            cls.data_type,
            cls.data_code,
            cls.data_checksum,
            cls.data_id,
            sequence,
            cls.payload
        )
        checksum = cls.check(packet)
        return struct.pack(
            '>BBHHH32s',
            cls.data_type,
            cls.data_code,
            checksum,
            cls.data_id,
            sequence,
            cls.payload
        )

    @staticmethod
    def check(data):
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

async def send(loop, packet, ip, sequence, timeout=2):
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

async def ping(loop, ip):
    '''
    '''

    print(f'ping {ip}')
    for i in range(0, 4):
        sequence = i + 1
        packet = Packer.pack(sequence)
        times = await send(loop, packet, ip, sequence)
        if times > 0:
            print('{}: 字节=32 时间={}ms'.format(ip, int(times * 1000)))
            await asyncio.sleep(0.7)
        else:
            print("请求超时。")
    return ip


async def main(loop):
    '''
    程序主循环
    '''

    tasks = []
    for ip in ip_network('192.168.0.0/24'):
        task = ping(loop, f'{ip}')
        tasks.append(task)
    dones, pendings = await asyncio.wait(tasks)

    for d in dones:
        print(f'done {d.result()}')

    for p in pendings:
        print(f'pending {p.result()}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
