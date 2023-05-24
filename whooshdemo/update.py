from whoosh.index import open_dir
from whoosh.qparser import QueryParser

idx = open_dir("indexdir")
writer = idx.writer()

# 这个很奇怪 是通过 ID(unique=True) 的字段去匹配，同时修改非匹配的字段。
writer.update_document(
    path=u"/path/to/dddd",
    title=u"First document, 中文2222",
)
writer.update_document(
    path=u"/path/to/dddd",
    title=u"First document, 中文2222",
)
writer.commit()
print(writer.doc_count())
