import platform
import sys
from chardet import detect
from subprocess import check_output, CalledProcessError

def get_run_encoding():
    sn = platform.system()
    if sn == 'Windows':
        co = check_output(['cmd', '/c', 'echo', '中文命令行输出'])
    elif sn == 'Linux':
        co = check_output(['echo', '中文命令行输出'])
    cd = detect(co)
    e = cd['encoding']
    print(co.decode(e))
    return e

print(get_run_encoding())


print('---')
print(sys.getfilesystemencoding())
