import os
import sys
import time
import importlib
import test_mpkgl
import threading

def m_list():
    r = {}
    for mn in sys.modules:
        m = importlib.import_module(mn)
        if hasattr(m, '__file__'):
            p = getattr(m, '__file__')
            s = os.stat(p)
            t = s.st_mtime_ns
            r[mn] = t
    return r

MT = m_list()

def tick():
    global MT
    while True:
        time.sleep(1)
        print('tick')
        nmt = m_list()
        for k, v in nmt.items():
            if MT[k] != v and k != '__main__':
                try:
                    m = importlib.import_module(k)
                    importlib.reload(m)
                    print(f'reload: {k}')
                except Exception as e:
                    print(e)
        MT = nmt

if __name__ == '__main__':
    thread = threading.Thread(target=tick)
    thread.daemon = True
    thread.start()
    while True:
        time.sleep(1)
        print('loop')
        try:
            test_mpkgl.my_test_func()
        except Exception as e:
            print(e)


