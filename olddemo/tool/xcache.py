import os
import shutil
from optparse import OptionParser

def clear_pycache(folder, deep=True):
    '''
    列举目录下的目录
    '''
    result = []
    dirname = os.path.abspath(folder)
    for i in os.listdir(dirname):
        path = os.path.abspath(dirname + '/' + i)
        if os.path.isdir(path):
            if i == '__pycache__':
                result.append(path)
                shutil.rmtree(path)
            elif deep:
                result.extend(clear_pycache(path, deep))
    return result

op = OptionParser('''清理 pycache 缓存''')
(options, args) = op.parse_args()

if __name__ == '__main__':
    f = args[0] if len(args) > 0 else '.'
    for r in clear_pycache(f):
        print(f'drop {r}')
