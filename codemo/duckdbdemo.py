# pip install duckdb

import duckdb

cursor = duckdb.connect()

print(cursor.execute('SELECT 44').fetchall())
