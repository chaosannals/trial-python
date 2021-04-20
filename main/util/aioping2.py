import asyncio
import aioping
import math
import time
from ipaddress import ip_network


async def ping(ip, timeout=10):
    try:
        delay = await aioping.ping(ip, timeout)
        return (ip, True, delay)
    except TimeoutError:
        return (ip, False, timeout)


async def main(loop):
    '''
    '''

    cc = 255
    ipn = list(ip_network('192.168.0.0/24'))[1:-1]
    ipc = math.ceil(len(ipn) / cc)
    ipg = [ipn[i * cc: (i + 1)* cc] for i in range(ipc)]
    result = []
    start = time.time()
    for ips in ipg:
        tasks = []
        for ip in ips:
            print(f'ping {ip}')
            task = ping(f'{ip}')
            tasks.append(task)
        dones, pendings = await asyncio.wait(tasks)
        print(f'dones: {len(dones)}; pendings: {len(pendings)}')
        for d in dones:
            ip, r, _ = d.result()
            if r: 
                result.append(ip)
    result.sort()
    end = time.time()
    print(f'time: {end - start}s')
    for ip in result:
        print(ip)
 
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()