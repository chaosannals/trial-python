import time
import asyncio
import threading


async def run_back_loop():
    '''
    次线程异步循环操作。
    '''
    while True:
        await asyncio.sleep(2)
        t = threading.current_thread()
        print('run_back_loop {}'.format(t))


def run_back():
    '''
    次线程。
    '''
    print('run_back')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.run_coroutine_threadsafe(run_back_loop(), loop)
    loop.run_forever()


def run_fore():
    '''
    主线程。
    '''
    thread = threading.Thread(target=run_back)
    thread.start()
    while True:
        time.sleep(3)
        t = threading.current_thread()
        print('run_fore {}'.format(t))


if __name__ == '__main__':
    run_fore()
