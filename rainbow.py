from hashlib import md5
from functools import reduce

RSET = '0123456789abcdefghijklmnopqrstuvwxyz'



def rainbow(h):
    '''
    1. 长度均匀
    2. 字符集
    3. 输入使用均匀
    '''
    l = reduce(lambda a, b: a + b, [ord(i) for i in h]) % 16
    r = []
    for i in range(l):
        pass
    return l




h = md5(b'123421s111111111ad33fasdf34123124324').hexdigest()
print(h)
r = rainbow(h)
print(r)