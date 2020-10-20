import time
import threading


def sum_1_to(n, i):
    '''
    一个耗时的累加计算。
    '''
    print('start: {}'.format(i))
    start = time.time()
    r = 0
    for i in range(n):
        r += i
    end = time.time()
    print('end {}: {}s'.format(i, end - start))
    return r


def new_daemon_thread(target, args):
    '''
    启动一个守护线程。
    '''

    thread = threading.Thread(target=target, args=args)
    thread.daemon = True
    thread.start()
    return thread


def main():
    '''
    由于 GIL 锁，导致 Python 解释器只能同时执行单线程的代码。
    每 100 个 Python 解释器命名切换一个线程执行。
    '''

    for i in range(4):
        new_daemon_thread(target=sum_1_to, args=(100000000, i))

    # 主进程任意输入退出。
    input('place input to exit:\n')


if __name__ == '__main__':
    main()
