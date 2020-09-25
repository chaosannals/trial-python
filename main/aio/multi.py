from asyncio import sleep, wait, get_event_loop, ensure_future

async def work(t):
    await sleep(t)
    print('time {}'.format(t))
    return t

def on_done(t):
    print(t.result())

async def main():
    # 协程
    coroutines = []
    for i in range(2):
        c = work(i)
        print(type(c))
        coroutines.append(c)
    await wait(coroutines)

    # 任务
    tasks = []
    for i in range(10):
        c = work(i)
        t = ensure_future(c)
        t.add_done_callback(on_done)
        print(type(t))
        tasks.append(t)
    await wait(tasks)



loop = get_event_loop()
loop.run_until_complete(main())
loop.close()
