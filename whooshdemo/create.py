from whoosh.fields import Schema, TEXT, ID
from whoosh.index import create_in

book_schema = Schema(
    title=TEXT(stored=True),
    path=ID(stored=True),
    content=TEXT,
)

# 创建 create_in 会导致整个数据库没了。使用 open_dir 插入数据和查询。
idx = create_in("indexdir", book_schema)
writer = idx.writer()
writer.add_document(
    title=u"First document, 中文",
    path=u"/path/to/dddd",
    content=u"this first doc 带中文信息",
)
writer.add_document(
    title=u"First document, 中文2324",
    path=u"/path/to/dddd",
    content=u"this first doc 带中文sfdsf信息",
)

# 提交修改
writer.commit()

# 取消修改
# writer.cancel()
