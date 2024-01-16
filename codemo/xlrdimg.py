# 不支持图片。

import os
import xlrd


HERE = os.path.dirname(__file__)

book = xlrd.open_workbook(os.path.join(HERE,"xlrdimg.xls"))

sh = book.sheet_by_index(0)

for rx in range(sh.nrows):
    print(sh.row(rx))