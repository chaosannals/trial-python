# pip install -i https://mirrors.aliyun.com/pypi/simple/ opencv-python

# python3.11 前需要手动安装此模块，不然没办法使用 imshow
# pip install  -i https://mirrors.aliyun.com/pypi/simple/  opencv-contrib-python

# pip install -i https://mirrors.aliyun.com/pypi/simple/  insightface
# pip install -i https://mirrors.aliyun.com/pypi/simple/  onnxruntime # cpu 装这个
# pip install onnxruntime-gpu # 有显卡装这个

# 首次执行时要开全局代理梯子，它要 github 上下载东西。

# 这个库使用了 numpy 1.20.0 以后被废弃，1.24.0 被删除的函数，要降低 numpy 的版本。
# pip install -i https://mirrors.aliyun.com/pypi/simple/ numpy==1.23.5


import cv2
import numpy as np
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

app = FaceAnalysis(
    providers=[
        # 'CUDAExecutionProvider', # 显卡
        'CPUExecutionProvider', # CPU
    ]
)
app.prepare(ctx_id=0, det_size=(640, 640))
img = ins_get_image('t1')
faces = app.get(img)
rimg = app.draw_on(img, faces)
#cv2.imwrite("./t1_output.jpg", rimg)
cv2.imshow("t1", rimg)
cv2.waitKey()
