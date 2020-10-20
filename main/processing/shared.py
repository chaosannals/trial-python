import time
import multiprocessing
from multiprocessing.shared_memory import SharedMemory
import numpy as np

def sum_list(n, length, i):
    '''
    一个耗时的累加计算。
    '''
    print('start: {}'.format(i))
    start = time.time()
    r = 0
    m = SharedMemory(name=n)
    a = np.ndarray((length, ), dtype=np.int64, buffer=m.buf)
    for j in a:
        r += j
    end = time.time()
    print('end {} = {}: {}s'.format(i, r, end - start))


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

    for i in range(4):
        new_process(target=sum_list, args=(memory.name, length, i))

    # 主进程任意输入退出。
    input('place input to exit:\n')


if __name__ == '__main__':
    main()
