import functools

def d_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        func(*args, **kwargs)
    return wrapper