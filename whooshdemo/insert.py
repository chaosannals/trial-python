from whoosh.index import open_dir
from faker import Faker

fake = Faker(['zh_CN', 'it_IT', 'en_US', 'ja_JP'])

# 插入
idx = open_dir("indexdir")
writer = idx.writer()

for i in range(4444):
    writer.add_document(
        title=f"First {fake.name()} {i}",
        path=f"/path/to/dddd/{i}",
        content=fake.text(),
        # 字段必须预先申明，不能像 mongodb 一样随意添加数据。添加动态字段
        #noinschema="aaaaaaaaa",
        anthor=fake.name(),
        address=fake.address(),

        # 动态字段
        dyn_no=f"number {i}",
        dyn_aaaa=f"动态字段 {i}",
        dyn_bbbb=f"动态字段1  {i * 2}",
    )
writer.add_document(
    title=u"First document, 中文23244444444444444",
    path=u"/path/to/dddd",
    content=u"this first doc 带中文sfdsf信息44444444444",
)
writer.commit()

# 打印 writer 操作的文档个数
print(writer.doc_count())
