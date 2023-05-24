from whoosh.index import open_dir
from whoosh.qparser import QueryParser


idx = open_dir("indexdir")
with idx.searcher() as searcher:
    # 默认只查了 前 10个。。
    query = QueryParser("title", idx.schema).parse("中文2222")
    # query = QueryParser("dyn_aaaa", idx.schema).parse("动态字段2")
    # query = QueryParser("dyn_bbbb", idx.schema).parse("动态字段1")
    results = searcher.search(query)
    print(results)
    for r in results:
        print(r)