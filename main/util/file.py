import os
import re


def list_file(folder, deep=False, nsort=False):
    '''
    列举目录下的文件
    '''

    result = []
    dirname = os.path.realpath(folder)
    for i in os.listdir(dirname):
        path = os.path.realpath(dirname + '/' + i)
        if os.path.isdir(path):
            if deep:
                result.extend(list_file(path))
        else:
            result.append(path)
    if nsort:
        sorted(result, key=lambda p: re.sub(r'\d+', lambda m: '{:010}'.format(int(m.group())), p))
    return result


def list_folder(folder, deep=False):
    '''
    列举目录下的目录
    '''
    result = []
    dirname = os.path.abspath(folder)
    for i in os.listdir(dirname):
        path = os.path.abspath(dirname + '/' + i)
        if os.path.isdir(path):
            result.append(path)
            if deep:
                result.extend(list_folder(path))
    return result

def haming_distance(a, b):
    '''
    汉明距离
    '''
    d = bin(int(a) ^ int(b))
    return d.count('1')

print(list_file('.'))
print(list_file('.', True))
print(list_folder('..'))
print(list_folder('..', True))
