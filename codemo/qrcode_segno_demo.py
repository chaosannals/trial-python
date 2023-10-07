# pip install segno
# pip install pillow
# pip install qrcode-artistic

import os
import segno

# 简单
qrcode = segno.make('Yellow Submarine')
qrcode.save('simple.png', scale=10)

# 色彩
qrcode.save(
    'color.png',
    dark="red",
    light="#4499ff",
    scale=10,
    border=10,
)

qrcode.save(
    'color2.png',
    dark="red",
    light="#4499ff",
    scale=10,
    border=10,
    finder_dark="yellow"
)

# 使用 qrcode-artistic 库生成 gif 图
here = os.path.dirname(__file__)

# to_artistic 由 qrcode-artistic 库扩展提供。
qrcode.to_artistic(
    background=os.path.join(here, 'bg.gif'),
    target='bg.out.gif',
    scale=8,
)

# PIL 处理图片

'''
二维码中心图片：
1. 四个边角没有被遮挡
2. 遮挡面积不超过三分之一
就可以通过容错矫正。
所以中心图片是直接遮挡在上面的。

二维码彩图：
1. 满足二维码规范
2. 前景色比背景色深即可（彩图在识别时应该是直接被转成灰色图了）。
'''
