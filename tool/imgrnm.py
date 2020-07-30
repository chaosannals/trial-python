import os
import re
import glob
import shutil
from optparse import OptionParser

def glob_file(folder, suffix=['png', 'jpg']):
    result = []
    for s in suffix:
        paths = glob.glob('{}/*.{}'.format(folder, s))
        result.extend(paths)
    return result

op = OptionParser('''
切割图片。
''')
op.add_option('-s', '--source',
              dest="source",
              type="string",
              action="store",
              default=os.getcwd(),
              metavar="SOURCE",
              help="图片源目录路径。"
              )
op.add_option('-t', '--target',
              dest="target",
              type="string",
              action="store",
              default='{}/rename'.format(os.getcwd()),
              metavar="TARGET",
              help="图片生成目录路径。"
              )
(options, args) = op.parse_args()

# 清空
if os.path.isdir(options.target):
    shutil.rmtree(options.target)
os.makedirs(options.target)

# 重命名
paths = glob_file(options.source)
for i, p in enumerate(sorted(paths, key=lambda p: re.sub(r'\d+', lambda m: '{:010}'.format(int(m.group())), p))):
    name = os.path.basename(p)
    suffix = name[name.rfind('.'):]
    d = '{}/{:04}{}'.format(options.target, i + 1, suffix)
    print('{} => {}'.format(p, d))
    shutil.copyfile(p, d)
    