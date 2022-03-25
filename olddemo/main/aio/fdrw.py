import asyncio
import functools
import os
import sys

if sys.platform.startswith("win"):
    if sys.version_info[0] > 3 or (sys.version_info[0] == 3 and sys.version_info[1] >= 8):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def minor(loop, i):
    p = f'temp/{i}.txt'
    future = loop.create_future()
    writer = open(p, 'w')
    def write(content, future):
        writer.write(content)
        writer.close()
        future.set_result(None)
        loop.remove_writer(writer)
    callback = functools.partial(
        write,
        content='123123',
        future=future
    )
    loop.add_writer(writer, callback)
    await future
        
    


async def main(loop):
    '''
    程序主循环
    '''

    tasks = []
    for i in range(20):
        task = minor(loop, i)
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