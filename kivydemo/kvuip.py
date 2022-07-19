import os
from glob import glob

def pick_kvfile(d):
    glob()

def build_init():
    '''
    
    '''
    pd = os.path.dirname(__file__)
    d = os.path.join(pd, 'kvui')
    ip = os.path.join(d, '__init__.py')
    with open(ip, 'w', encoding='utf8') as writer:
        writer.write('from kivy.lang import Builder\n\n')
        for p in glob(f'{d}/**.kv'):
            rp = os.path.relpath(p, pd).replace('\\', '/')
            writer.write(f"Builder.load_file('{rp}')\n")

if '__main__' == __name__:
    build_init()
