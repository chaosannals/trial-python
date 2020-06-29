import os
from optparse import OptionParser
from PIL import Image

op = OptionParser('''
ICO 文件生成。
''')
op.add_option('-t', '--target',
              dest="target",
              type="string",
              action="store",
              default='{}/target.ico'.format(os.getcwd()),
              metavar="TARGET",
              help="图片生成路径。"
              )
(options, args) = op.parse_args()

for path in args:
    im = Image.open(path)
    im.save(options.target, 'ico', sizes=[(256,256), (400,400)])
else:
    Image.init()
    print(Image.SAVE.keys())