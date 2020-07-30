import re
import random
from optparse import OptionParser

CHARSET='''
qwertyuiop
asdfghjkl
zxcvbnm
QWERTYUIOP
ASDFGHJKL
ZXCVBNM
1234567890
'''

op = OptionParser('''
密码随机生成。
''')

op.add_option("-l", '--length',
    dest="length",
    type="int",
    action="store",
    default=12,
    metavar="LENGTH",
    help="密码长度。"
)
(options, args) = op.parse_args()

charset = re.sub(r'[\r\n]', '', CHARSET)
maxindex = len(charset) - 1
result = []
for i in range(options.length):
    index = random.randint(0, maxindex)
    result.append(charset[index])

print(''.join(result))
