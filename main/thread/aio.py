import re
import time
import asyncio
import threading

loop_able = True

async def run_back_loop(loop):
    '''
    次线程异步循环操作。
    '''
    while loop_able:
        await asyncio.sleep(2)
        t = threading.current_thread()
        print('run_back_loop {}'.format(t))


def run_back():
    '''
    次线程，用于异步处理。
    '''

    print('run_back')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_back_loop(loop))
    loop.close()


def run_fore():
    '''
    主线程，没有异步循环。
    '''
    thread = threading.Thread(target=run_back)
    thread.daemon = True
    thread.start()
    while True:
        text = input('place input:\n')
        t = threading.current_thread()
        print('run_fore {}'.format(t))
        if text.find('exit') >= 0:
            global loop_able
            loop_able = False
            break


if __name__ == '__main__':
    run_fore()
