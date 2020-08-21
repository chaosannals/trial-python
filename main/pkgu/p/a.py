def d_1(method):
    print(dir(method))
    print(method.__qualname__)
    return method

class A:
    '''
    '''

    def __init__(self):
        '''
        '''

    @d_1
    def m1(self):
        print('m1')