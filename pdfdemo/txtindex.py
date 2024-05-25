import re
import os
from glob import glob


txt_paths = glob('*.txt')

for txt_path in txt_paths:
    if txt_path.endswith('index.txt'):
        continue
    dirname = os.path.dirname(txt_path)
    filename = os.path.basename(txt_path)
    [name, suffix] = os.path.splitext(filename)
    index_path = os.path.join(dirname, f'{name}.index{suffix}')
    print(f'{txt_path} => {index_path}')
    chapters = []
    with open(txt_path, 'r') as reader:
        lines = reader.readlines()
        print(f'总计: {len(lines)} 行')
        for i, line in enumerate(lines):
            m = re.match(r'第.+[章卷节]', line)
            if m is not None:
                chapter = f'[第 {i:6} 行] {line}'
                print(chapter)
                chapters.append(chapter)
    with open(index_path, 'w', encoding='utf8') as writer:
        writer.writelines(chapters)
