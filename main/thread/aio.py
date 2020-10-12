import re
import time
import asyncio
import threading

loop_able = True


def new_daemon_thread(target):
    '''
    启动一个守护线程。
    '''

    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()


def run_client():
    '''
    '''


def run_server():
    '''
    '''


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

    new_daemon_thread(run_back)
    new_daemon_thread(run_server)
    new_daemon_thread(run_client)

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
