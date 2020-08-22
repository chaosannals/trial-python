from functools import wraps
from importlib import import_module


def ddd(name):
    def ddd_1(func):
        '''
        '''
        nlen = len(func.__name__) + 1
        cname = func.__qualname__[:-nlen]
        m = import_module(func.__module__)
        if not hasattr(m, '___ddd___'):
            setattr(m, '___ddd___', [])
        m.___ddd___.append((cname, func.__name__, name))
        return func

    return ddd_1


class AC:
    '''
    '''

    def __init__(self):
        '''
        '''
        self.name = 'AAA'

    @ddd('hello')
    def afunc(self):
        print(self.name)


i = AC()
i.afunc()
m = import_module(__name__)
print(m.___ddd___)
print(m.__loader__.is_package(m.__name__))