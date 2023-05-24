from whoosh.index import open_dir

# 插入
idx = open_dir("indexdir")
writer = idx.writer()
writer.add_document(
    title=u"First document, 中文444444444444",
    path=u"/path/to/dddd",
    content=u"this first doc 带中文信息",
    # 字段必须预先申明，不能像 mongodb 一样随意添加数据。添加动态字段
    #noinschema="aaaaaaaaa",

    # 动态字段
)
writer.add_document(
    title=u"First document, 中文23244444444444444",
    path=u"/path/to/dddd",
    content=u"this first doc 带中文sfdsf信息44444444444",
)
writer.commit()

# 打印 writer 操作的文档个数
print(writer.doc_count())
