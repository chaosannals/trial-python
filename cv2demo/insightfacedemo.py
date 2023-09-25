# pip install -i https://mirrors.aliyun.com/pypi/simple/ opencv-python

# python3.11 前需要手动安装此模块，不然没办法使用 imshow
# pip install  -i https://mirrors.aliyun.com/pypi/simple/  opencv-contrib-python

# pip install -i https://mirrors.aliyun.com/pypi/simple/  insightface
# pip install -i https://mirrors.aliyun.com/pypi/simple/  onnxruntime # cpu 装这个
# pip install onnxruntime-gpu # 有显卡装这个

# 首次执行时要开全局代理梯子，它要 github 上下载东西。

# 这个库使用了 numpy 1.20.0 以后被废弃，1.24.0 被删除的函数，要降低 numpy 的版本。
# pip install -i https://mirrors.aliyun.com/pypi/simple/ numpy==1.23.5

import re
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
    # allowed_modules=[ # 可以通过设置跳过某些流程
    #     'detection', # 侦察（必须）
    #     'recognition', # 识别（如果没用到此功能可去掉）
    # ],
)
app.prepare(ctx_id=0, det_size=(640, 640))

# root_dir 在 python3.9 没有这个参数，要 python3.11 才有。
# imgs = glob(r'*/*.jpg', root_dir=here, recursive=True)
# pngs = glob(r'*/*.png', root_dir=here, recursive=True)
imgs = glob(f'{here}/*/*.*', recursive=True)
imgs = filter(lambda p: re.match(r'(.*?)(?<!face)\.(png|jpg|jpeg)$', p, re.I) is not None, imgs)

# print([i for i in imgs])
# exit()

for img_path in imgs:
    # img = ins_get_image('t1')
    # cv2.imshow('raw', img)

    img = cv2.imread(img_path)

    faces = app.get(img)
    rimg = app.draw_on(img, faces)

    print(f'{img_path}:')
    for face in faces:
        print(f"face keys：{face.keys()}")
        print(f"脸区域（bbox）：{face['bbox']}")
        print(f"五官（kps）： {face['kps']}")
        print(f"性别（gender）：{face['gender']}")
        print(f"年龄（age）：{face['age']}")
        print(f"特征长（embedding）：{len(face['embedding'])}") # 512维向量，欧氏距离小于 1.24 认为同一人
        print(f"3D关键点68个（landmark_3d_68）：{len(face['landmark_3d_68'])}")
        print(f"2D关键点106个（landmark_2d_106）：{len(face['landmark_2d_106'])}")
        print(f"识别分（det_score）：{face['det_score']}")

    if len(faces) > 0:
        img_name = os.path.splitext(img_path)
        out_path = f"{img_name[0]}-face{img_name[1]}"
        print(f'out: {out_path}')
        cv2.imwrite(out_path, rimg)

    cv2.imshow(img_path, rimg)

cv2.waitKey()
