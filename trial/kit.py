import time

def timing(action):
    '''
    耗时计算。
    '''

    start = time.time()
    action()
    end = time.time()
    return end - start
