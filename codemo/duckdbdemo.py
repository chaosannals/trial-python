# pip install duckdb
# C++版本的只提供 duckdb.exe
# 目录下 居然没找到 duckdb.exe
# TODO 查 python 版本的实现方式

import duckdb

cursor = duckdb.connect()

print(cursor.execute('SELECT 44').fetchall())
