from whoosh.index import open_dir

# 插入
idx = open_dir("indexdir")
writer = idx.writer()
writer.add_document(
    title=u"First document, 中文444444444444",
    path=u"/path/to/dddd",
    content=u"this first doc 带中文信息",
    # 字段必须预先申明，不能像 mongodb 一样随意添加数据。
    #noinschema="aaaaaaaaa",
)
writer.add_document(
    title=u"First document, 中文23244444444444444",
    path=u"/path/to/dddd",
    content=u"this first doc 带中文sfdsf信息44444444444",
)
writer.commit()
