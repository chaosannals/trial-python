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
              default='{}/cutting'.format(os.getcwd()),
              metavar="TARGET",
              help="图片生成目录路径。"
              )
op.add_option('-r', '--row',
              dest="row",
              type="int",
              action="store",
              default=1,
              metavar="ROW",
              help="切割行数。"
              )
op.add_option('-c', '--column',
              dest="column",
              type="int",
              action="store",
              default=2,
              metavar="COLUMN",
              help="切割行列数。"
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
    suffix = name[name.rfind('.'):]
    perfix = name[:name.rfind('.')]
    w = im.width / options.column
    h = im.height / options.row
    print('({}) {} 切割成：'.format(i, p))
    for y in range(options.row):
        for x in range(options.column):
            xyname = '{}/{}-{}-{}{}'.format(
                options.target,
                perfix,
                x,
                y,
                suffix
            )
            xyim = im.crop((
                x * w,
                y * h,
                (x + 1) * w,
                (y + 1) * h
            ))
            xyim.save(xyname)
            print('{} => {}'.format(i, xyname))
