from whoosh.index import open_dir
from whoosh.qparser import QueryParser


idx = open_dir("indexdir")
with idx.searcher() as searcher:
    # 默认只查了 前 10个。。
    query = QueryParser("content", idx.schema).parse("first")
    results = searcher.search(query)
    print(results)
    for r in results:
        print(r)