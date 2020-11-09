import time
from PyQt5.QtCore import *

class QtMT(QThread):
    '''
    Qt 的多线程，都被 GIL 锁住了。
    '''

    def __init__(self, n, i):
        '''
        初始化。
        '''

        super().__init__()
        self.n = n
        self.i = i
        self.start()

    def __del__(self):
        self.wait()

    def run(self):
        '''
        线程主程序。
        '''
        print('start: {}'.format(self.i))
        start = time.time()
        r = 0
        for j in range(self.n):
            r += j
        end = time.time()
        print('end {}: {}s'.format(self.i, end - start))

def main():
    '''
    '''

    for i in range(6):
        QtMT(100000000, i)

if __name__ == '__main__':
    main()

        