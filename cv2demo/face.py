# pip install  -i https://mirrors.aliyun.com/pypi/simple/  opencv-python

# python3.11 前需要手动安装此模块，不然没办法使用 imshow
# pip install  -i https://mirrors.aliyun.com/pypi/simple/  opencv-contrib-python

import os
import cv2
from glob import glob

here = os.path.dirname(__file__)
model_dir = os.path.dirname(cv2.data.__file__)
# model_haar_path = os.path.join(model_dir, 'haarcascade_frontalface_default.xml') # 误识别太多，空气都识别了。
# model_haar_path = os.path.join(model_dir, 'haarcascade_frontalface_alt.xml') # 这个不会误识别，但是也有漏掉
model_haar_path = os.path.join(model_dir, 'haarcascade_frontalface_alt2.xml') # 这个不会误识别，但是也有漏掉

print(f'here: {here}')
print(f"haar path: {model_haar_path}")

face_cascade = cv2.CascadeClassifier(model_haar_path)

# root_dir 在 python3.9 没有这个参数，要 python3.11 才有。
# imgs = glob(r'*/*.jpg', root_dir=here, recursive=True)
# pngs = glob(r'*/*.png', root_dir=here, recursive=True)
imgs = glob(f'{here}/*/*.jpg', recursive=True)
pngs = glob(f'{here}/*/*.png', recursive=True)
imgs.extend(pngs)

for img_path in imgs:
    print(f'img path: {img_path}')
    # img = cv2.imread(f'{here}/{img_path}')
    img = cv2.imread(f'{img_path}')
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow(f'result {img_path}', img)

cv2.waitKey()
