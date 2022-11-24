from dataclasses import dataclass
from os.path import basename, splitext, exists
from os import makedirs
from glob import glob
import gzip
import json
import struct
import numpy as np
import cv2

@dataclass
class MnistData:
    '''
    
    '''
    label: np.ndarray
    image: np.ndarray


class MnistDataSet:
    '''
    
    '''

    def __init__(self, labels_path, images_path, label_set_count):
        '''
        
        '''

        self.labels_path = labels_path
        self.images_path = images_path
        self.label_set_count = label_set_count
        self.data_set = None

    def count(self):
        '''
        
        '''
        if self.data_set is None:
            return 0
        return len(self.data_set)

    def get_one(self, index) -> MnistData:
        '''
        
        '''
        if self.data_set is None:
            self.ensure_data_set()
        return self.data_set[index]

    def ensure_data_set(self):
        '''
        
        '''
        if self.data_set is not None:
            return

        labels, label_count = self.load_labels()
        images, image_count, *_ = self.load_images()
        if label_count != image_count:
            raise Exception("标签和图片数目不符")
        self.data_set = []
        for i in range(label_count):
            label = labels[i]
            image = images[i]
            self.data_set.append(MnistData(label, image))

    def load_labels(self):
        '''
        
        '''
        if not exists(self.labels_path):
            raise Exception("无效的标签路径")
        with gzip.open(self.labels_path, 'r') as reader:
            data = reader.read()
            magic_number, = struct.unpack(">i", data[:4])
            if magic_number != 2049: # 标签
                raise Exception('不是有效的标签文件')

            label_count, = struct.unpack('>i', data[4:8])
            labels = []
            for i in data[8:]:
                label = np.zeros(self.label_set_count) + 0.01
                label[i] = 0.99
                labels.append(label)
            if label_count != len(labels):
                raise Exception('标签数不对')

            return labels, label_count

    def load_images(self):
        '''
        
        '''
        if not exists(self.labels_path):
            raise Exception("无效的图片路径")

        with gzip.open(self.images_path, 'r') as reader:
            data = reader.read()
            magic_number, = struct.unpack(">i", data[:4])
            if magic_number != 2051: # 图片
                raise Exception("不是有效的图片文件")
            image_count, row_count, column_count = struct.unpack('>iii', data[4:16])
            image_size = row_count * column_count
            start = 16
            images = []
            for i in range(image_count):
                image_data = [px for px in data[start:start + image_size]]
                image_array = np.array(image_data, dtype=np.uint8).reshape(row_count, column_count, 1)
                start += image_size
                images.append(image_array.flatten())
            return images, image_count, row_count, column_count
                


def unzip_mnist(zip_pattern):
    '''
    
    '''
    for p in glob(zip_pattern):
        bn = basename(p)
        name, suffix = splitext(bn)
        use_kind, file_kind, *_ = name.split('-')
        print(f'{p} => {use_kind} {file_kind} ({name})[{suffix}]')

        with gzip.open(p, 'r') as reader:
            data = reader.read()
            magic_number, = struct.unpack(">i", data[:4])
            if magic_number == 2049: # 标签
                label_count, = struct.unpack('>i', data[4:8])
                print(f'标签数：{label_count}')
                labels = [i for i in data[8:]]
                with open(f'temp/{use_kind}.json', 'w') as writer:
                    json.dump(labels, writer)
            elif magic_number == 2051: # 图片
                d = f'temp/{use_kind}'
                makedirs(d, exist_ok=True)
                image_count, row_count, column_count = struct.unpack('>iii', data[4:16])
                print(f'图片数：{image_count} 图片格式：{row_count} * {column_count}')
                image_size = row_count * column_count
                start = 16
                for i in range(image_count):
                    image_data = [px for px in data[start:start + image_size]]
                    image_array = np.array(image_data, dtype=np.uint8).reshape(row_count, column_count, 1)
                    cv2.imwrite(f'{d}/{i}.jpg', image_array)
                    start += image_size
            else:
                print('不是有效的文件类型')
                print(magic_number)
