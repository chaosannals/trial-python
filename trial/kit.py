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


def reduce(vs, op='or'):
    '''
    批量 or 得结果
    '''

    if op == 'or':
        return functools.reduce(lambda x, y: x or y, vs)
    if op == 'and':
        return functools.reduce(lambda x, y: x and y, vs)
    raise Exception('不是有效的合并操作')


def in_dict(d, ks, reop=None):
    '''
    批量判断是否在字典里。
    '''

    r = []
    dks = d.keys()
    for k in ks:
        r.append(k in dks)
    if reop == None:
        return r
    return reduce(r, reop)
