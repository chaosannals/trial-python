import time
import datetime
import functools
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


def in_dict(d, ks):
    '''
    批量判断是否在字典里。
    '''

    r = []
    dks = d.keys()
    for k in ks:
        r.append(k in dks)
    return r


def batch_or(vs):
    '''
    批量 or 得结果
    '''

    return functools.reduce(lambda x, y: x or y, vs)


def batch_and(vs):
    '''
    批量 and 得结果
    '''

    return functools.reduce(lambda x, y: x and y, vs)
