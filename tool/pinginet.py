import asyncio
import argparse
import aioping
from ipaddress import ip_network


async def ping(ip, timeout=10):
    try:
        delay = await aioping.ping(ip, timeout)
        return (ip, True, delay)
    except TimeoutError:
        return (ip, False, timeout)


async def main(net):
    '''
    '''

    tasks = []
    for ip in list(ip_network(net))[1:-1]:
        # print(f'ping {ip}')
        task = ping(f'{ip}')
        tasks.append(task)
    dones, pendings = await asyncio.wait(tasks)
    print(f'dones: {len(dones)}; pendings: {len(pendings)}')
    for d in dones:
        ip, r, _ = d.result()
        if r:
            print(ip)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ping internal net.')
    parser.add_argument(
        '--inet',
        type=str,
        help='internal net address',
        default='192.168.0.0/24'
    )
    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args.inet))
    loop.close()
