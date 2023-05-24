from whoosh.index import open_dir
from whoosh.qparser import QueryParser

idx = open_dir("indexdir")
writer = idx.writer()
query = QueryParser("content", idx.schema).parse("dyn")
r = writer.delete_by_query(query)
writer.commit()
print(r)
