from whoosh.index import open_dir
from whoosh.qparser import QueryParser


idx = open_dir("indexdir")
with idx.searcher() as searcher:
    # 默认只查了 前 10个。。
    query = QueryParser("title", idx.schema).parse("First")
    # query = QueryParser("dyn_aaaa", idx.schema).parse("动态字段2")
    # query = QueryParser("dyn_bbbb", idx.schema).parse("动态字段1")
    results = searcher.search(query, terms=True)
    print(results)
    if results.has_matched_terms():
        print(results.matched_terms())
        for hit in results:
            print(hit.matched_terms())
    for r in results:
        print(r)

    print('=================================================')
    # collector 可以做数据采集限制，有很多种。
    # collapse 指定的字段结果集合不要 collapse_limit 条相同数据。
    c = searcher.collector(collapse="title", collapse_limit=1)
    searcher.search_with_collector(query, c)
    results = c.results()
    for r in results:
        print(r)