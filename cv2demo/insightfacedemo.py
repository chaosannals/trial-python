# pip install -i https://mirrors.aliyun.com/pypi/simple/ opencv-python

# python3.11 前需要手动安装此模块，不然没办法使用 imshow
# pip install  -i https://mirrors.aliyun.com/pypi/simple/  opencv-contrib-python

# pip install -i https://mirrors.aliyun.com/pypi/simple/  insightface
# pip install -i https://mirrors.aliyun.com/pypi/simple/  onnxruntime # cpu 装这个
# pip install onnxruntime-gpu # 有显卡装这个

# 首次执行时要开全局代理梯子，它要 github 上下载东西。

# 这个库使用了 numpy 1.20.0 以后被废弃，1.24.0 被删除的函数，要降低 numpy 的版本。
# pip install -i https://mirrors.aliyun.com/pypi/simple/ numpy==1.23.5

import os
import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image
from glob import glob

here = os.path.dirname(__file__)

app = FaceAnalysis(
    providers=[
        # 'CUDAExecutionProvider', # 显卡
        'CPUExecutionProvider', # CPU
    ],
    allowed_modules=[
        'detection',
        'recognition'
    ],
)
app.prepare(ctx_id=0, det_size=(640, 640))

# root_dir 在 python3.9 没有这个参数，要 python3.11 才有。
# imgs = glob(r'*/*.jpg', root_dir=here, recursive=True)
# pngs = glob(r'*/*.png', root_dir=here, recursive=True)
imgs = glob(f'{here}/*/*.jpg', recursive=True)
pngs = glob(f'{here}/*/*.png', recursive=True)
imgs.extend(pngs)

for img_path in imgs:
    # img = ins_get_image('t1')
    # cv2.imshow('raw', img)

    img = cv2.imread(img_path)

    faces = app.get(img)
    rimg = app.draw_on(img, faces)

    print(f'{img_path}:')
    for face in faces:
        print(f"face keys: {face.keys()}")
        print(f"脸区域（bbox）: {face['bbox']}")
        print(f"五官（kps）: {face['kps']}")

    #cv2.imwrite("./t1_output.jpg", rimg)
    cv2.imshow(img_path, rimg)

cv2.waitKey()
