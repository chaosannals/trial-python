# 这个库 0.2.0 ，不支持图片。
# 还会直接把公式变成结果了。。。

import os
from xls2xlsx import XLS2XLSX

HERE = os.path.dirname(__file__)

x2x = XLS2XLSX(os.path.join(HERE, "xlrdimg.xls"))
x2x.to_xlsx(os.path.join(HERE, "xlrdimg.xlsx"))