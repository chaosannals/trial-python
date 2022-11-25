from glob import glob
from os.path import basename, splitext
import numpy as np
import cv2

def load_selfwrite(files_pattern, width=28, height=28):
    result = []
    for p in glob(files_pattern):
        bn = basename(p)
        n, _ = splitext(bn)
        _, label_raw = n.split('-')
        label = np.zeros(10) + 0.01
        label[int(label_raw)] = 0.99
        image_array = cv2.imread(p)
        image_array = cv2.resize(image_array, (width, height))
        image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
        image_data = image_array.reshape(width * height)
        result.append((label, image_data, label_raw))
    return result
        
