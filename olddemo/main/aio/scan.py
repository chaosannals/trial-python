from asyncio import wait, get_event_loop, open_connection
from contextvars import ContextVar

hosts = ContextVar('hosts')
hosts.set({})

async def scan(host, port):
    href= '{}:{}'.format(host, port)
    print('scan start {}'.format(href))
    try:
        reader, writer = await open_connection(host, port)
        writer.write('Test \r\n'.encode('utf-8'))
        await writer.drain()
        result = await reader.read(1000)
        r = hosts.get()
        r[href] = result
        hosts.set(r)
        writer.close()
        await writer.wait_closed()
    except Exception as e:
        print('scan failed: {}'.format(e))
        

host = 'baidu.com'
loop = get_event_loop()
chunk = 100
for j in range(10):
    tasks = [scan(host, i + j * chunk) for i in range(1, chunk + 1)]
    loop.run_until_complete(wait(tasks))
loop.close()

r = hosts.get()
print(r.keys())