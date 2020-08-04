import os
import sys
import glob
from PyQt5 import uic

here = os.path.realpath(os.path.dirname(sys.argv[0]))
print('开始查找 Qt5 Ui 文件：{}'.format(here))

def list_ui_file(folder):
    '''
    列举目录下的 Qt5 Ui 文件
    '''

    result = []
    dirname = os.path.realpath(folder)
    for i in os.listdir(dirname):
        p = os.path.realpath(dirname + '/' + i)
        if os.path.isdir(p):
            result.extend(list_ui_file(p))
        elif p[-3:] == '.ui':
            result.append(p)
    return result

for p in list_ui_file(here):
    d = os.path.dirname(p)
    n = os.path.basename(p)
    pyp = os.path.realpath('{}/ui_{}.py'.format(d, n[0:-3]))
    print('编译文件 {} => {}'.format(p, pyp))
    with open(pyp, 'w', encoding='utf-8') as w:
        uic.compileUi(p, w)