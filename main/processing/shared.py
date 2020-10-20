import time
import multiprocessing
from multiprocessing.shared_memory import SharedMemory, ShareableList
import numpy as np

def sum_by_memory(n, length, i):
    '''
    共享内存，一个耗时的累加计算。
    '''
    print('start by memory: {}'.format(i))
    start = time.time()
    r = 0
    m = SharedMemory(name=n)
    a = np.ndarray((length, ), dtype=np.int64, buffer=m.buf)
    for j in a:
        r += j
    end = time.time()
    print('end by memory {} = {}: {}s'.format(i, r, end - start))

def sum_by_list(n, i):
    '''
    共享列表，一个耗时的累加计算。
    '''

    print('start by list: {}'.format(i))
    start = time.time()
    r = 0
    for j in ShareableList(name=n):
        r += j
    end = time.time()
    print('end by list {} = {}: {}s'.format(i, r, end - start))

def new_process(target, args):
    '''
    启动一个守护线程。
    '''

    process = multiprocessing.Process(target=target, args=args)
    process.start()
    return process


def main():
    '''
    主函数。
    '''

    length = 10000000
    memory = SharedMemory(create=True, size=8 * length)
    a = np.ndarray((length,),dtype=np.int64, buffer=memory.buf)
    a[:] = range(length)

    # 大小不能超过 10M，有诸多限制。
    b = ShareableList(range(10000))

    for i in range(4):
        new_process(target=sum_by_memory, args=(memory.name, length, i))
    for i in range(4):
        new_process(target=sum_by_list, args=(b.shm.name, i))

    # 主进程任意输入退出。
    input('place input to exit:\n')


if __name__ == '__main__':
    main()
