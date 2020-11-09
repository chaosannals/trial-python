import time
import vthread

@vthread.pool(6)
def sum_1_to(n, i):
    '''
    一个耗时的累加计算。
    '''
    print('start: {}'.format(i))
    start = time.time()
    r = 0
    for j in range(n):
        r += j
    end = time.time()
    print('end {}: {}s'.format(i, end - start))
    return r

def main():
    '''
    vthread 管理包，都被 GIL 锁住了。
    '''

    for i in range(6):
        sum_1_to(100000000, i)

if __name__ == '__main__':
    main()
