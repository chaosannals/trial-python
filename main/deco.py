from functools import wraps

def tt_1(name):
    print('tt_1 a')
    def decorator(func):
        print('tt_1 b')
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('tt_1')
            data.append(('tt_1', func))
            return func(*args, **kwargs)
        return wrapper
    return decorator

data = []

def tt_2(name):
    print('tt_2 a')
    def decorator(func):
        print('tt_2 b')
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('tt_2')
            data.append(('tt_2', func))
            return func(*args, **kwargs)
        return wrapper
    return decorator

def tt_3(func):
    print('tt_3 a')
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('tt_3')
        data.append(('tt_3', func))
        return func(*args, **kwargs)
    return wrapper

@tt_3
@tt_1('aaaa')
@tt_2('bbb')
def tf():
    print('tf')

tf()

for n, f in data:
    # print(n)
    print(f.__name__)