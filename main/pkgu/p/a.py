def d_1(method):
    # for k in dir(method):
    #     v = getattr(method, k)
    #     print(k)
    #     print(v)
    return method

class ddd:
    def __init__(self, method):
        self.method = method
    
    def __get__(self, instance, cls):
        print('ddd def')
        print(cls)
        def wrapper(*args, **kwargs):
            print('dd call')
            return self.method(instance, *args, **kwargs)
        print(wrapper.__name__)
        return wrapper

class A:
    '''
    '''

    def __init__(self):
        '''
        '''

    @ddd
    @d_1
    def m1(self):
        print('m1')