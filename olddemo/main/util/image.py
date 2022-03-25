import os
import glob
import shutil
from PIL import Image

def images_compress(source, target):
    if not os.path.isdir(target):
        os.mkdirs(target)
    paths = glob.glob(source + '/*')
    result = {}
    for p in glob.glob(source + '/*'):
        name = os.path.basename(p)
        suffix = name[name.rfind('.'):]
        if suffix in ['.jpg', '.jpeg', '.png', '.gif']:
            im = Image.open(p)
            np = '{}/{}'.format(target, name)
            im.save(np)
            result[p] = np
    return result