import os
from math import floor

def ccl_block_bare_list(inp, outd, c):
    '''
    文件分段暴露
    '''
    
    if not os.path.isdir(outd):
        os.makedirs(outd)

    with open(inp, 'rb') as reader:
        all = reader.read()
        size = len(all)

        bs = floor(size / c)
        print(f'block size: {bs}')
        for i in range(c):
            s = i * bs
            e = s + bs

            outp = f'{outd}/h{i}.exe'
            with open(outp, 'wb') as writer:
                for _ in range(s):
                    writer.write(b'\0')
                writer.write(all[s:e])
                for _ in range(size-e):
                    writer.write(b'\0')
                print(f'out: {outp}')

def ccl_block_bare(inp, outp, s, e):
    '''
    
    '''

    with open(inp, 'rb') as reader:
        all = reader.read()
        size = len(all)

        if s >= size or e >= size:
            return False

        with open(outp, 'wb') as writer:
            for _ in range(s):
                writer.write(b'\0')
            writer.write(all[s:e])
            for _ in range(size-e):
                writer.write(b'\0')
            print(f'out: {outp}')