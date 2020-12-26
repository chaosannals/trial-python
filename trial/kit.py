import time
import datetime
import pytz

def timing(action):
    '''
    耗时计算。
    '''

    start = time.time()
    action()
    end = time.time()
    return end - start

def get_now(tz='PRC', fmt='%Y-%m-%d %H:%M:%S'):
    '''
    获取当前时间。
    '''

    tz = pytz.timezone(tz)
    dt = datetime.datetime.now(tz)
    return dt.strftime(fmt)

    