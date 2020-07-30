import os
import glob
import shutil
from PIL import Image
from optparse import OptionParser


def glob_file(folder, suffix=['png', 'jpg']):
    result = []
    for s in suffix:
        paths = glob.glob('{}/*.{}'.format(folder, s))
        result.extend(paths)
    return result


op = OptionParser('''
压缩图片。
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
              default='{}/resize'.format(os.getcwd()),
              metavar="TARGET",
              help="图片生成目录路径。"
              )
op.add_option('-r', '--rate',
              dest="rate",
              type="float",
              action="store",
              default=0.9,
              metavar="RATE",
              help="图片缩小比例。"
              )
(options, args) = op.parse_args()

# 清空
if os.path.isdir(options.target):
    shutil.rmtree(options.target)
os.makedirs(options.target)

# 处理
paths = glob_file(options.source)
for i, p in enumerate(paths):
    im = Image.open(p)
    name = os.path.basename(p)
    np = '{}/{}'.format(options.target, name)
    w, h = im.size
    im.resize(
        (
            int(w * options.rate),
            int(h * options.rate)
        )
    ).save(np)
    print('{} => {}'.format(p, np))
