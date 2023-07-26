from time import time_ns
import lancedb

uri = "./.lancedb"
db = lancedb.connect(uri)
tns = db.table_names()
print(tns)
tn = 'my_table'

now = time_ns()
if (tn not in tns):
    # 创建表的时候就确定了字段结构了。
    # 之后通过 add 添加字段无效。
    table = db.create_table(
        tn,
        data=[
            {"vector": [3.1, 4.1], "item": "foo", "price": 10.0, "createAt": now},
            {"vector": [5.9, 26.5], "item": "bar", "price": 20.0, "createAt": now},
        ],
    )
else:
    table = db.open_table(tn)
    table.add(
        data=[
            {"vector": [3.1, 4.1], "item": "foo", "price": 10.0, "createAt": now},
            {"vector": [5.9, 26.5], "item": "bar", "price": 20.0, "createAt": now},
        ],
    )
    df = table.to_pandas()
    print(df)