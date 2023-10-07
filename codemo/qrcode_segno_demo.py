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

# gif 图
here = os.path.dirname(__file__)

# to_artistic 由 qrcode-artistic 库扩展提供。
qrcode.to_artistic(
    background=os.path.join(here, 'bg.gif'),
    target='bg.out.gif',
    scale=8,
)