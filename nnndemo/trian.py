from os.path import basename, splitext
from os import makedirs
from glob import glob
from nnn.base import NumNeuralNetwork
import gzip
import json
import struct
import numpy as np
import cv2

def unzip_mnist():
    '''
    
    '''
    for p in glob('assets/*.gz'):
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
            # with open(n, 'wb') as writer:
            #     writer.write(data)



def main():
    unzip_mnist()

    n = NumNeuralNetwork()
    r = n.train([1.0, 0.5, -1.5], [1.0, 0.5, -1.5])
    print(r)

if '__main__' == __name__:
    main()